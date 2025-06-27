import csv
from re import search
from tkinter import filedialog, Tk
import os
import platform
import io
from pandas.errors import EmptyDataError
import jcamp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import sqlite3
from my_new import compound_lookup

# par= []
def Chem1():
    syt = float(
        input("What system is it:\n1=Adiabatic\n2=Isothermal\n3=Isochoric\n4=Isobaric\n5=Free Space expansion\n"))
    while syt > 5 or syt < 1:
        syt = int(
            input("What system is it:\n1=Adiabatic\n2=Isothermal\n3=Isochoric\n4=Isobaric\n5=Free Space expansion\n"))
    if syt == 1.0:
        que = str(input("What do you want to Calculate i.e ft for finaltemperature: "))
        dar = que.replace(" ", "")
        Cal = dar.lower()
        par = []
        if Cal == "ft":
            try:
                num = int(input("How many parameters are given: "))
                while num >= 5:
                    num = int(input("How many parameters are given: "))
            except:
                print("Invalid input! Enter a valid number less than 5")
            else:
                for i in range(1, num + 1):
                    parameter = str(input(f"Enter no {i} parameter :"))
                    no_space = parameter.replace(" ", "")
                    para = no_space.lower()
                    par.append(para)
                if "it" in par and "iv" in par and "fv" in par:
                    print(
                        "Always remember for \nmonoatomic gas Cv=(3/2)R, Cp=Cv+R\nFor diatomic gas Cv=(5/2)R, Cp = Cv+R\nfor polyatomic gas Cv=3R,Cp=Cv+R")
                    Gamma = float(input("Enter the value of γ =Cp/Cv: "))
                    initialtemperature = float(input("Enter the Initial Temperature(in Kelvin) i.e:it: "))
                    initialvolume = float(input("Enter the Initial Volume(in centimeter cube):i.e iv: "))
                    finalvolume = float(input("Enter the final volume(in centimeter cube) :i.e fv: "))
                    z = (initialvolume / finalvolume)
                    a = float(Gamma - 1)
                    b = z ** a
                    finalltemperature = initialtemperature * b
                    roundabout = round(finalltemperature, 2)
                    print(f"Final Tmperature {roundabout} K")
                elif "ip" in par and "fp" in par and "it" in par:
                    print(
                        "Always remember for \nmonoatomic gas Cv=(3/2)R, Cp=Cv+R\nFor diatomic gas Cv=(5/2)R, Cp = Cv+R\nfor polyatomic gas Cv=3R,Cp=Cv+R")
                    Gamma = float(input("Enter the value of γ =Cp/Cv: "))
                    initialtemperature = float(input("Enter the Initial Temperature(in Kelvin):i.e it: "))
                    initialpressure = float(input("Enter the Initial Pressure(in bar):i.e ip: "))
                    finalpressure = float(input("Enter the final Pressure(in bar):i.e fp: "))
                    z = (finalpressure / initialpressure)
                    a = float(Gamma - 1)
                    p = z ** a
                    x = (initialtemperature) ** Gamma
                    y = (p) * (x)
                    finaltemperature = y ** (1 / Gamma)
                    roundabout = round(finaltemperature, 2)
                    print(f"Final Tmperature {roundabout} K")
        elif Cal == "it":
            try:
                num = int(input("How many parameters are given: "))
                while num >= 5:
                    num = int(input("How many parameters are given: "))
            except:
                print("Invalid input! Enter a valid number less than 5")
            else:
                for i in range(1, num + 1):
                    parameter = str(input(f"Enter no {i} parameter :"))
                    no_space = parameter.replace(" ", "")
                    para = no_space.lower()
                    par.append(para)
                if "ft" in par and "iv" in par and "fv" in par:
                    print(
                        "Always remember for \nmonoatomic gas Cv=(3/2)R, Cp=Cv+R\nFor diatomic gas Cv=(5/2)R, Cp = Cv+R\nfor polyatomic gas Cv=3R,Cp=Cv+R")
                    Gamma = float(input("Enter the value of γ =Cp/Cv: "))
                    finaltemperature = float(input("Enter the final Temperature(in Kelvin): "))
                    initialvolume = float(input("Enter the Initial Volume(in centimeter cube): "))
                    finalvolume = float(input("Enter the final volume(in centimeter cube): "))
                    z = (initialvolume / finalvolume)
                    a = float(Gamma - 1)
                    b = z ** a
                    initialtemperature = finaltemperature / b
                    roundabout = round(initialtemperature, 2)
                    print(f"Final Temperature {roundabout} K")
                elif "ip" in par and "fp" in par and "ft" in par:
                    print(
                        "Always remember for \nmonoatomic gas Cv=(3/2)R, Cp=Cv+R\nFor diatomic gas Cv=(5/2)R, Cp = Cv+R\nfor polyatomic gas Cv=3R,Cp=Cv+R")
                    Gamma = float(input("Enter the value of γ =Cp/Cv: "))
                    finaltemperature = float(input("Enter the Initial Temperature(in Kelvin): "))
                    initialpressure = float(input("Enter the Initial Pressure(in bar): "))
                    finalpressure = float(input("Enter the final Pressure(in bar): "))
                    z = (initialpressure / finalpressure)
                    a = float(Gamma - 1)
                    p = z ** a
                    x = (finaltemperature) ** Gamma
                    y = (p) * (x)
                    initialtemperature = y ** (1 / Gamma)
                    roundabout = round(initialtemperature, 2)
                    print(f"Initial Tmperature {roundabout} K")
        elif Cal == "iv":
            try:
                num = int(input("How many parameters are given: "))
                while num >= 5:
                    num = int(input("How many parameters are given: "))
            except:
                print("Invalid input! Enter a valid number less than 5")
            else:
                for i in range(1, num + 1):
                    parameter = str(input(f"Enter no {i} parameter :"))
                    no_space = parameter.replace(" ", "")
                    para = no_space.lower()
                    par.append(para)
                if "ft" in par and "it" in par and "fv" in par:
                    print(
                        "Always remember for \nmonoatomic gas Cv=(3/2)R, Cp=Cv+R\nFor diatomic gas Cv=(5/2)R, Cp = Cv+R\nfor polyatomic gas Cv=3R,Cp=Cv+R")
                    Gamma = float(input("Enter the value of γ =Cp/Cv: "))
                    finaltemperature = float(input("Enter the final Temperature(in Kelvin): "))
                    initialtemperature = float(input("Enter the Initial temperature(in centimeter cube): "))
                    finalvolume = float(input("Enter the final volume(in centimeter cube): "))
                    z = (finaltemperature / initialtemperature)
                    a = float(Gamma - 1)
                    b = (finalvolume) ** a
                    c = z * b
                    initialvolume = c ** (1 / a)
                    roundabout = round(initialvolume, 2)
                    print(f"Initial Volume {roundabout} cm^3")
                elif "fv" in par and "ip" in par and "fp" in par:
                    print(
                        "Always remember for \nmonoatomic gas Cv=(3/2)R, Cp=Cv+R\nFor diatomic gas Cv=(5/2)R, Cp = Cv+R\nfor polyatomic gas Cv=3R,Cp=Cv+R")
                    Gamma = float(input("Enter the value of γ =Cp/Cv: "))
                    initialpressure = float(input("Enter the Initial Pressure(in N/m^2): "))
                    finalvolume = float(input("Enter the Final Volume(in meter cube): "))
                    finalpressure = float(input("Enter the final pressure(in N/m^2): "))
                    z = (finalpressure / initialpressure)
                    b = (finalvolume) ** (Gamma)
                    c = z * b
                    initialvolume = c ** (1 / Gamma)
                    roundabout = round(initialvolume, 2)
                    print(f"Initial Volume {roundabout} m^3")
        elif Cal == "fv":
            try:
                num = int(input("How many parameters are given: "))
                while num >= 5:
                    num = int(input("Should be less than 5 parameters: "))
            except:
                print("Invalid input! Enter a valid number less than 5")
            else:
                for i in range(1, num + 1):
                    parameter = str(input(f"Enter no {i} parameter :"))
                    no_space = parameter.replace(" ", "")
                    para = no_space.lower()
                    par.append(para)
                if "ft" in par and "iv" in par and "it" in par:
                    print(
                        "Always remember for \nmonoatomic gas Cv=(3/2)R, Cp=Cv+R\nFor diatomic gas Cv=(5/2)R, Cp = Cv+R\nfor polyatomic gas Cv=3R,Cp=Cv+R")
                    Gamma = float(input("Enter the value of γ =Cp/Cv: "))
                    finaltemperature = float(input("Enter the final Temperature(in Kelvin): "))
                    initialtemperature = float(input("Enter the Initial Temperature(in kelvin): "))
                    initialvolume = float(input("Enter the initial volume(in centimeter cube): "))
                    z = (initialtemperature / finaltemperature)
                    a = float(Gamma - 1)
                    b = (initialvolume) ** a
                    c = z * b
                    finalvolume = c ** (1 / a)
                    roundabout = round(finalvolume, 2)
                    print(f"Initial Volume {roundabout} cm^3")
                elif "iv" in par and "ip" in par and "fp" in par:
                    print(
                        "Always remember for \nmonoatomic gas Cv=(3/2)R, Cp=Cv+R\nFor diatomic gas Cv=(5/2)R, Cp = Cv+R\nfor polyatomic gas Cv=3R,Cp=Cv+R")
                    Gamma = float(input("Enter the value of γ =Cp/Cv: "))
                    initialpressure = float(input("Enter the Initial Pressure(in N/m^2): "))
                    initialvolume = float(input("Enter the Initial Volume(in meter cube): "))
                    finalpressure = float(input("Enter the final pressure(in N/m^2): "))
                    z = (initialpressure / finalpressure)
                    b = (initialvolume) ** (Gamma)
                    c = z * b
                    finalvolume = c ** (1 / Gamma)
                    roundabout = round(finalvolume, 2)
                    print(f"Final Volume {roundabout} m^3")
        elif Cal == "fp":
            try:
                num = int(input("How many parameters are given: "))
                while num >= 5:
                    num = int(input("Should be less than 5 parameters: "))
            except:
                print("Invalid input! Enter a valid number less than 5")
            else:
                for i in range(1, num + 1):
                    parameter = str(input(f"Enter no {i} parameter :"))
                    no_space = parameter.replace(" ", "")
                    para = no_space.lower()
                    par.append(para)
                if "ft" in par and "ip" in par and "it" in par:
                    print(
                        "Always remember for \nmonoatomic gas Cv=(3/2)R, Cp=Cv+R\nFor diatomic gas Cv=(5/2)R, Cp = Cv+R\nfor polyatomic gas Cv=3R,Cp=Cv+R")
                    Gamma = float(input("Enter the value of γ =Cp/Cv: "))
                    finaltemperature = float(input("Enter the final Temperature(in Kelvin): "))
                    initialtemperature = float(input("Enter the Initial Temperature(in kelvin): "))
                    initialpressure = float(input("Enter the Initial Pressure(in bar): "))
                    z = (finaltemperature / initialtemperature)
                    a = float(Gamma - 1)
                    b = (initialpressure) ** a
                    c = z ** Gamma
                    x = c * b
                    finalpressure = x ** (1 / a)
                    roundabout = round(finalpressure, 2)
                    print(f"Final Pressure:  {roundabout} bar")


#Chem1()


def save_spectra_to_db(db_path, compound_name, ir_df, fft_df):
    # Convert dataframes to CSV strings (1 row each)
    ir_csv_str = ir_df.to_csv(index=False)
    fft_csv_str = fft_df.to_csv(index=False)

    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS compound_spectra (
            compound_name TEXT PRIMARY KEY,
            ir_data TEXT,
            fft_data TEXT
        )
    ''')

    # Insert or replace
    cursor.execute('''
        INSERT OR REPLACE INTO compound_spectra (compound_name, ir_data, fft_data)
        VALUES (?, ?, ?)
    ''', (compound_name, ir_csv_str, fft_csv_str))

    conn.commit()
    conn.close()
    print(f"✅ Compound '{compound_name}' has been saved.")
#save_spectra_to_db(db_path, compound_name, ir_df, fft_df)
# Hide the Tkinter root window
def MainMenu():
    while True:
        try:
            select = int(input(
                "\nMain Menu:\n"
                "1: Download JCAMP IR spectrum (NIST)\n"
                "2: Perform Fourier Transform on IR data\n"
                "3: Chemistry calculations\n"
                "4: Identify an Unknown Compound through the IR csv file\n"
                "0: Exit\n"
                "Enter your choice: "
            ))

            if select == 1:
                def find_jcamp_dx_link(compound_name):
                    compound_name = compound_name.replace(' ', '+')  # Replace spaces with "+" for URL format
                    search_url = f"https://webbook.nist.gov/cgi/cbook.cgi?Name={compound_name}&Units=SI"

                    try:
                        # Step 2: Send a request to fetch the web page
                        response = requests.get(search_url)

                        # Check if the response was successful
                        response.raise_for_status()  # Raise an error for bad status codes
                    except requests.exceptions.RequestException as e:
                        return f"Error fetching data from NIST: {e}"

                    # Step 3: Parse the HTML content of the page
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Step 4: Find the IR spectrum link
                    jcamp_link = None
                    for link in soup.find_all('a', href=True):
                        if ('IR' in link['href'] or 'jcamp' in link['href']):  # Look for IR or jcamp-related links
                            jcamp_link = "https://webbook.nist.gov" + link['href']
                            break

                    if not jcamp_link:
                        return f"No IR spectrum found for {compound_name} on NIST."

                    return jcamp_link

                def find_jcamp_for_multiple_compounds():
                    compound_input = input("Enter the names of compounds, separated by commas: ")

                    # Step 2: Split the input string into a list of compound names
                    compound_list = [compound.strip() for compound in compound_input.split(',')]

                    # Step 3: Loop through the list of compounds and get their JCAMP-DX links
                    results = {}
                    for compound in compound_list:
                        print(f"Searching for {compound}...")
                        result = find_jcamp_dx_link(compound)
                        results[compound] = result
                        print(f"Result for {compound}: {result}")

                    # Step 4: Return the results
                    return results
                results = find_jcamp_for_multiple_compounds()

            elif select == 2:
                file_name = input("Enter JDX filename (with or without '.jdx'): ").strip()
                if not file_name.endswith('.jdx'):
                    file_name += '.jdx'

                username = input("Enter your computer username: ").strip()

                # Detect platform and construct path
                if "microsoft" in platform.uname().release.lower():  # WSL
                    downloads_path = os.path.join("/mnt/c/Users", username, "Downloads")
                else:  # Native Windows
                    downloads_path = os.path.join("C:\\Users", username, "Downloads")

                file_path = os.path.join(downloads_path, file_name)

                if not os.path.isfile(file_path):
                    print(f"❌ File not found at: {file_path}")
                    continue

                # Read file lines
                with open(file_path, "r") as file:
                    lines = file.readlines()

                yunits_line = next((line for line in lines if "##YUNITS=" in line), None)

                if yunits_line and "ABSORBANCE" in yunits_line.upper():
                    y_factor = 1.0
                    delta_x = 4.0  # default spacing

                    for line in lines:
                        if line.startswith("##YFACTOR="):
                            y_factor = float(line.split("=")[1].strip())
                        elif line.startswith("##DELTAX="):
                            delta_x = float(line.split("=")[1].strip())

                    xydata_index = next(i for i, line in enumerate(lines) if "##XYDATA=" in line)
                    data_lines = lines[xydata_index + 1:]

                    wavenumbers, absorbances = [], []

                    for line in data_lines:
                        parts = line.strip().split()
                        if not parts or not parts[0].replace('.', '', 1).isdigit():
                            continue
                        try:
                            start_x = float(parts[0])
                            y_vals = [int(y) * y_factor for y in parts[1:]]
                            x_vals = [start_x + i * delta_x for i in range(len(y_vals))]
                            wavenumbers.extend(x_vals)
                            absorbances.extend(y_vals)
                        except ValueError:
                            continue

                    transmittances = 10 ** (-np.array(absorbances))

                else:
                    # Try reading transmittance using jcamp
                    try:
                        data = jcamp.jcamp_readfile(file_path)
                        wavenumbers = data.get("x", [])
                        transmittances = data.get("y", [])

                        if len(wavenumbers) == 0 or len(transmittances) == 0:
                            print("⚠️ No spectral data found.")
                            continue
                    except Exception as e:
                        print(f"❌ Failed to read JDX file: {e}")
                        continue

                # --- Save to CSV ---
                output_csv = input("Enter output CSV filename (with or without '.csv'): ").strip()
                if not output_csv.endswith(".csv"):
                    output_csv += ".csv"
                csv_path = os.path.join(downloads_path, output_csv)
                compound_name = input("Enter compound name correctly.\n : ")
                compound = f"{compound_name}_ir.csv"
                # downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
                csv_path = os.path.join(downloads_path, compound)
                db_path = os.path.join(downloads_path, "compound_spectra.db")

                df = pd.DataFrame({
                    "Wavenumber (cm⁻¹)": wavenumbers,
                    "Transmittance": transmittances
                })
                df = df.sort_values(by="Wavenumber (cm⁻¹)")
                df["Wavenumber (cm⁻¹)"] = df["Wavenumber (cm⁻¹)"].round(1)
                df['Transmittance'] = df['Transmittance'].clip(lower=1e-6)
                df['Transmittance'] = df['Transmittance'].round(4)
                df.to_csv(csv_path, index=False)
                print(f"✅ CSV saved at: {csv_path}")

                # === PLOT SECTION ===
                intensity = df["Transmittance"].values
                wn = df["Wavenumber (cm⁻¹)"].values

                # FFT
                n = len(intensity)
                fft_vals = np.fft.fft(intensity)
                fft_mag = np.abs(fft_vals)
                half_n = n // 2 + 1
                fft_mag = 2 * fft_mag[:half_n] / n
                fft_mag[0] /= 2  # fix DC

                F = np.arange(1, half_n + 1)
                my_fft = pd.DataFrame({
                    "Frequency Index": F,
                    "FFT Magnitude": fft_mag
                })
                fft_csv_path = csv_path.replace(".csv", "_fft.csv")
                my_fft.to_csv(fft_csv_path, index=False)

                print(f"FFT results saved to: {csv_path}")

                save_spectra_to_db(db_path, compound_name, df, my_fft)

                # Plot
                plt.figure(figsize=(12, 6))

                plt.subplot(2, 1, 1)
                plt.plot(wn, intensity, color='darkred')
                plt.xlim([3800, 370])
                plt.xticks(np.arange(3800, 369, -200))
                plt.xlabel("Wavenumber (cm⁻¹)")
                plt.ylabel("Transmittance")
                plt.title("IR Spectrum")
                plt.grid(True)

                plt.subplot(2, 1, 2)
                plt.vlines(F[1:], 0, fft_mag[1:], color='blue')
                plt.scatter(F[1:], fft_mag[1:], color='blue', s=10)
                plt.xlim([0, 150])
                plt.xlabel("Frequency (a.u.)")
                plt.ylabel("Amplitude")
                plt.title("FFT of IR Spectrum")
                plt.grid(True)

                plt.tight_layout()
                plt.show()

            elif select == 3:
                #from pack.Chemistry import Chem1
                Chem1()
            elif select == 4:
                #from my_new import compound_lookup
                compound_lookup()
            elif select == 0:
                print("Logging out... 👋")
                break

            else:
                print("Invalid selection. Try again.")
        except ValueError:
            print("❌ Please enter a valid number.")

MainMenu()



