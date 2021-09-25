using System;


 namespace HelloWorld
{
   public class Order
   {

      public static void Third()
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
                              Console.WriteLine("Enter your phone number");
                                    phone = long.Parse(Console.ReadLine());
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

                         
               class Storage

          {
              //This is a default empty constructor
                    public void  Ware() {}
                     //Constructor overloading
                    public void Ware(string name)
                       {this.name = name;
                       }

                       public void Ware(string name,long phone,double Total,double Total3,double number)
                         
                         {
                            this.name = name;
                            this.phone = phone;
                            this.Total = Total;
                            this.Total3 = Total3;
                            this.number = number;

                         }
                          //This is an example of property
                    public string name   {get; set;}
                    public long phone    {get; set;}
                    public double Total  {get; set;}
                    public double Total3 {get; set;}
                    public double number {get; set;}

               
                  public override string ToString()
                  {
                    return $"Name:{this.name}, Phone:{this.phone}, Total:{this.Total}, Total3: {this.Total3}, Number:{this.number}";

                  }

          }
                    

              
}