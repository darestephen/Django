using System;


namespace HelloWorld
{
   public class Program
    {

        static void Main(string[] args)
        {        
            string input = "";
            bool exit = false;

         do 
        {
            Console.WriteLine("Welcome to BOP WAREHOUSE");
            Console.WriteLine("No 1 leading Warehouse in the United States");
            Console.WriteLine("Enter [1] for our Menus");
            Console.WriteLine("Enter [2] to leave and read our reviews");
            Console.WriteLine("Enter [3] to login or Create an account");
            Console.WriteLine("Enter [4] to continue as a guest");
            Console.WriteLine("Enter [0] to exit");

            input = Console.ReadLine();

            switch(input)
             {

                 case "1":
                            Console.WriteLine("You're about to read and view our reviews");
           
                   break;

                case "2":
                   Console.WriteLine("You're about to read and view our reviews");
                   break;

                case "3":
                   Console.WriteLine("You're about to Login or Create an Account");
                   break;
                case "4":
                   Console.WriteLine("You're about to Continue as a guest");
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
