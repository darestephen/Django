import pandas as pd
from tkinter import filedialog, Tk
import pandas as pd
import numpy as np
import sqlite3
import os
import platform
import io
from pandas.errors import EmptyDataError

# Hide the Tkinter root window
def compound_lookup():
    root = Tk()
    root.withdraw()

    # Prompt user to select a CSV file
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    # Check if user selected a file
    try:
        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError("❌ Uploaded CSV is empty.")
        if "Wavenumber (cm⁻¹)" not in df.columns or "Transmittance" not in df.columns:
            raise ValueError("❌ Invalid format. Expected columns: 'Wavenumber (cm⁻¹)' and 'Transmittance'.")

        print("✅ Valid CSV loaded.")
    except EmptyDataError:
        print("❌ The selected CSV file is empty.")
        exit(1)
    except Exception as e:
        print(f"❌ Failed to load CSV: {e}")
        exit(1)
    if file_path:
        try:
            df = pd.read_csv(file_path)
            print(f"✅ File loaded from: {file_path}")
            print(df.head())  # Show first few rows
        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
    else:
        print("⚠️ No file was selected.")


    def compute_similarity(trans1, trans2):
        min_len = min(len(trans1), len(trans2))
        trans1 = trans1[:min_len]
        trans2 = trans2[:min_len]

        # Mean squared error
        mse = np.mean((trans1 - trans2) ** 2)
        return mse
    def identify_compound_from_csv(uploaded_csv_path, db_path):
        # Load uploaded CSV
        uploaded_df = pd.read_csv(uploaded_csv_path)
        uploaded_trans = uploaded_df["Transmittance"].values

        required_column = "Transmittance"
        if required_column not in uploaded_df.columns:
            raise ValueError(f"❌ Uploaded file is missing required column: '{required_column}'")

        uploaded_trans = uploaded_df[required_column].values

        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get all compounds
        cursor.execute("SELECT compound_name, ir_data FROM compound_spectra")
        records = cursor.fetchall()
        conn.close()

        best_match = None
        lowest_error = float("inf")

        for name, ir_csv in records:
            try:
                ir_df = pd.read_csv(io.StringIO(ir_csv))
                if "Transmittance" not in ir_df.columns:
                    raise ValueError(f"❌ Stored spectrum for '{name}' is missing 'Transmittance' column.")

                #ir_df = pd.read_csv(pd.compat.StringIO(ir_csv))
                db_trans = ir_df["Transmittance"].values

                error = compute_similarity(uploaded_trans, db_trans)

                if error < lowest_error:
                    lowest_error = error
                    best_match = name
            except Exception as e:
                print(f"Error processing {name}: {e}")

        return best_match, lowest_error
    uploaded_csv_path = file_path
    username = input("Enter your computer username: ").strip()

                    # Detect platform and construct path
    if "microsoft" in platform.uname().release.lower():  # WSL
        downloads_path = os.path.join("/mnt/c/Users", username, "Downloads")
    else:  # Native Windows
        downloads_path = os.path.join("C:\\Users", username, "Downloads")

                    #file_path = os.path.join(downloads_path, file_name)
    db_path = os.path.join(downloads_path, "compound_spectra.db")

    match_name, similarity_score = identify_compound_from_csv(uploaded_csv_path, db_path)

    if match_name:
        print(f"🧪 Best match: {match_name} (error score: {similarity_score:.4f})")
    else:
        print("❌ No match found.")
#compound_lookup()