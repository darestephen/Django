using System;

namespace Models
{
     public class Storage

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
