using System;
using System.Collections.Generic;

 namespace HelloWorld
{
   public class Resto
   {

      public static void Second()
      {        
          List<Contact>MyContacts = new List<Contact>();

          MyContacts.Add(new Contact
          {
             name = "Remmy Martin",
             quantity = "369",
             price = "$7689 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "REMMY VSOP",
             quantity = "356",
             price = "$9689 per Carton"

          });
          MyContacts.Add(new Contact
          {
             name = "HENNESSY VSOP",
             quantity = "240",
             price = "$8453 per Carton"

          });
          MyContacts.Add(new Contact
          {
             name = "AMSTERDAM",
             quantity = "724",
             price = "$1780 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "JAMESON",
             quantity = "545",
             price = "$5470 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "RED LABEL",
             quantity = "115",
             price = "$6571 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "FIREBALL",
             quantity = "420",
             price = "$3451 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "CIROC",
             quantity = "550",
             price = "$4205 per Carton"

          });

          MyContacts.Add(new Contact
          {
             name = "MALIBU COCONUT",
             quantity = "1002",
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