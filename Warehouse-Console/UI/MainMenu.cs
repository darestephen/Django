using System;
using System.Collections.Generic;
using Models;

 namespace UI
{
   public class MainMenu : IMenu
   {

      public void Start()
      {        
                        string input = "";
                        bool exit = false;

                     do 
         {
                        Console.WriteLine("Welcome to BOP WAREHOUSE");
                        Console.WriteLine("No 1 leading Liqour Warehouse in the United States");
                        Console.WriteLine("Enter [1] to View our stocks");
                        Console.WriteLine("Enter [2] to leave and read our reviews");
                        Console.WriteLine("Enter [3] to make an order");
                        Console.WriteLine("Enter [0] to exit");

                        input = Console.ReadLine();

                        switch(input)
                        {

                           case "1":
                                     new WarehouseMenu().Start(); 
                              break;

                           case "2":
                              Console.WriteLine("You're about to read and view our reviews");
                              break;

                           case "3":
                               Console.WriteLine("You're about to make an order");
                               new WarehouseMenu().Start();
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

}
                  
                  