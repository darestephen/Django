using System;
using Models;
using System.Collections.Generic;

 namespace UI
{
   public class WarehouseMenu :IMenu
   {
        public void Start()
        {
              var Myinstance = new Resto();
                        var Instance = new Order();
                           string value = " ";
                        bool exit = false;

                     do 
         {
                        Console.WriteLine("Welcome to BOP WAREHOUSE");
                        Console.WriteLine("No 1 leading Liqour Warehouse in the United States");
                        Console.WriteLine("Enter [1] for our Warehouse Stocks");
                        Console.WriteLine("Enter [2] Proceed to Read and Leave Reviews!");
                        Console.WriteLine("Enter [3] Proceed to make orders");
                        Console.WriteLine("Enter [0] to exit");
        
                    value = Console.ReadLine();
                        switch(value)
                        {

                           case "1":
                                     Console.WriteLine("You'll be viewing our Menus");  
                                     Myinstance.Second();
                              break;

                           case "2":
                              Console.WriteLine("You're about to read and view our reviews");
                              break;

                           case "3":
                               Console.WriteLine("You're ready to make an order");
                                Instance.Third();
                              break;
                     
                           case "0":
                              Console.WriteLine("Go back to MainMenu");
                              exit = true;
                              break;
                           default:
                              Console.WriteLine("Invalid Number!");
                              break;
                           }
                        
         }while(!exit);
      
        }

                 
                public class Resto
   {

      public void Second()
      {        
          List<Contact>MyContacts = new List<Contact>();

          MyContacts.Add(new Contact
          {
             Name = "Remmy Martin",
             quantity = "369 Cartons in Stock",
             price = "$7689 per Carton"

          });

          MyContacts.Add(new Contact
          {
             Name = "REMMY VSOP",
             quantity = "356 Cartons in Stock",
             price = "$9689 per Carton"

          });
          MyContacts.Add(new Contact
          {
             Name = "HENNESSY VSOP",
             quantity = "240 Cartons in Stock",
             price = "$8453 per Carton"

          });
          MyContacts.Add(new Contact
          {
             Name = "AMSTERDAM",
             quantity = "724 Cartons in Stock",
             price = "$1780 per Carton"

          });

          MyContacts.Add(new Contact
          {
             Name = "JAMESON",
             quantity = "545 Cartons in Stock",
             price = "$5470 per Carton"

          });

          MyContacts.Add(new Contact
          {
             Name = "RED LABEL",
             quantity = "115 Cartons in Stock",
             price = "$6571 per Carton"

          });

          MyContacts.Add(new Contact
          {
             Name = "FIREBALL",
             quantity = "420 Cartons in Stock",
             price = "$3451 per Carton"

          });

          MyContacts.Add(new Contact
          {
             Name = "CIROC",
             quantity = "550 Cartons in Stock",
             price = "$4205 per Carton"

          });

          MyContacts.Add(new Contact
          {
             Name = "MALIBU COCONUT",
             quantity = "1002 Cartons in Stock",
             price = "$825 per Carton"

          });
          
        foreach (var Contact in MyContacts)
        {
            Console.WriteLine(Contact.Name);
            Console.WriteLine(Contact.quantity);
            Console.WriteLine(Contact.price);
            Console.WriteLine("=========================");
        }
            
    
      }
      
    class Contact
     {
       public string Name  {get; set;}
       public string quantity {get; set;}
       public string price{get; set;} 

     }
    
   }

       public class Order
   {

      public void Third()
        {
             double num2;
            double num3;
               double number; 
               double Total;
               double num1;
                 double num4;
                 double num5;
                double num6;
                 double promocode = 896.24;
                double Total3;
                string name = "";
                long phone;

                              Console.WriteLine("Dear Valued Customer,please fill the details below to begin your order");
                              Console.WriteLine("Enter your name below");
                                       name = Console.ReadLine();
                                      if (name == " ")
                                      {
                                         Console.WriteLine("Name can't be empty!Enter you name");
                                           name = Console.ReadLine();
                                      }
                                      else
                                      {
                                          Console.WriteLine("Enter your phone number");
                                    phone = long.Parse(Console.ReadLine());
                                      }
                                      
                               Console.WriteLine("[1] Enter the cartons of Hennessy VSOP");                         
                          number = int.Parse(Console.ReadLine());
                             num1 = (8453 * number);
                                 if (number >= 0)
                                 {
                                     Console.WriteLine("Number of HENNESSY VSOP: {0} \n Amount for your quantity: {1}" , number , num1.ToString("C"));
                                 }
                                
                                 else
                                 {
                                     Console.WriteLine("Continue to your next order!");
                                 }

                        Console.WriteLine("[2] Enter the cartons of  REMMY VSOP");
                         number = int.Parse(Console.ReadLine());
                                 num2 = (9689 * number);
                                 if (number >= 0)
                                 {
                                     Console.WriteLine("Number of HENNESSY VSOP: {0} \n Amount for your quantity: {1}" , number , num2.ToString("C"));
                                 }
                                
                                 else
                                 {
                                     Console.WriteLine("Continue to your next order!");
                                 }
                                

                        Console.WriteLine("[3] Enter the cartons of AMSTERDAM");
                        number = int.Parse(Console.ReadLine());
                                 num3 = (1780 * number);
                                 if (number >= 0)
                                 {
                                     Console.WriteLine("Number of HENNESSY VSOP: {0} \n Amount for your quantity: {1}" , number , num3.ToString("C"));
                                 }
                                
                                 else
                                 {
                                     Console.WriteLine("Continue to your next order!");
                                 }
                                 
                        Console.WriteLine("[4] Enter the cartons of JAMESON");
                        number = int.Parse(Console.ReadLine());
                                 num4 = (5470 * number);
                                 if (number >= 0)
                                 {
                                     Console.WriteLine("Number of HENNESSY VSOP: {0} \n Amount for your quantity: {1}" , number , num4.ToString("C"));
                                 }
                                
                                 else
                                 {
                                     Console.WriteLine("Continue to your next order!");
                                 }
                                
                        Console.WriteLine("[5] Enter the cartons of RED LABEL");
                        number = int.Parse(Console.ReadLine());
                                 num5 = (6571 * number);
                                 if (number >= 0)
                                 {
                                     Console.WriteLine("Number of HENNESSY VSOP: {0} \n Amount for your quantity: {1}" , number , num5.ToString("C"));
                                 }
                                
                                 else
                                 {
                                     Console.WriteLine("Continue to your next order!");
                                 }
                                
                        Console.WriteLine(" [6] Enter the cartons of FIREBALL");
                        number = int.Parse(Console.ReadLine());
                                 num6 = (3451 * number);    
                                 if (number >= 0)
                                 {
                                     Console.WriteLine("Number of FIREBALL: {0} \n Amount for your quantity: {1}" , number , num6.ToString("C"));
                                 }
                                
                                 else
                                 {
                                     Console.WriteLine("Continue to your next order!");
                                 }

                                    Console.WriteLine("==============================================");

                               Total = (num1 + num2 + num3 + num4 +num5 + num6);
                                
                                   if (Total >=7000.00 )
                                   {
                                       Total3 = (Total-promocode);

                                       Console.WriteLine("Total cost is : {0} \n New Discounted Total : {1}" ,Total.ToString("C"),Total3.ToString("C"));
                                   }
                              
                                   else
                                   {
                                             Console.WriteLine("Your total is : {0}" ,Total.ToString("C"));

                                   }
                          
                              Console.WriteLine("==============================================");
                         
                        Console.WriteLine("Enter any key to go back to the home page");
                          Console.ReadLine();

        }
               

    }

                         
          


   }

}
