using System;
using System.Collections.Generic;

 namespace HelloWorld
{
   public class Program
   {

      public static void Main(string[] args)
      {        
                        string input = "";
                        bool exit = false;

                     do 
         {
                        Console.WriteLine("Welcome to BOP WAREHOUSE");
                        Console.WriteLine("No 1 leading Liqour Warehouse in the United States");
                        Console.WriteLine("Enter [1] for our Menus");
                        Console.WriteLine("Enter [2] to leave and read our reviews");
                        Console.WriteLine("Enter [3] to make an order");
                        Console.WriteLine("Enter [0] to exit");

                        input = Console.ReadLine();

                        switch(input)
                        {

                           case "1":
                                    Resto.Second();  
                              break;

                           case "2":
                              Console.WriteLine("You're about to read and view our reviews");
                              break;

                           case "3":
                              Order.Third();
                              break;
                     
                           case "0":
                              Console.WriteLine("We're sorry to see you leave");
                              exit = true;
                              break;
                           default:
                              Console.WriteLine("Invalid Number!");
                              break;
                           }
                        
         }while(!exit);
      }
            
   }

                public class Resto
   {

      public static void Second()
      {        
         int quantity;
          List<Contact>MyContacts = new List<Contact>();

          MyContacts.Add(new Contact
          {
             name = "Remmy Martin",
             quantity = "369 Cartons in Stock",
             price = "$7689 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "REMMY VSOP",
             quantity = "356 Cartons in Stock",
             price = "$9689 per Carton"

          });
          MyContacts.Add(new Contact
          {
             name = "HENNESSY VSOP",
             quantity = "240 Cartons in Stock",
             price = "$8453 per Carton"

          });
          MyContacts.Add(new Contact
          {
             name = "AMSTERDAM",
             quantity = "724 Cartons in Stock",
             price = "$1780 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "JAMESON",
             quantity = "545 Cartons in Stock",
             price = "$5470 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "RED LABEL",
             quantity = "115 Cartons in Stock",
             price = "$6571 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "FIREBALL",
             quantity = "420 Cartons in Stock",
             price = "$3451 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "CIROC",
             quantity = "550 Cartons in Stock",
             price = "$4205 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "MALIBU COCONUT",
             quantity = "1002 Cartons in Stock",
             price = "$825 per Carton"

          });
          
        foreach (var Contact in MyContacts)
        {
            Console.WriteLine(Contact.name);
            Console.WriteLine(Contact.quantity);
            Console.WriteLine(Contact.price);
            Console.WriteLine("=========================");
        }
            
    
      }
      
    class Contact
     {
       public string name  {get; set;}
       public string quantity {get; set;}
       public string price{get; set;} 

     }
    
   }
                  
}
                  
                  
