using System;
using System.Collections.Generic;

namespace WarehouseMenus
{
    public class Program
    {
        static void Main(string[] args)
        {
        List<Props>Myitems=new List<Props>(items , number ,price);
           Myitems.Add(new Props
           {
               Myitems.items = "Amsterdam",
               Myitems.number = "120 cartons",
               Myitems.price = "$468 per carton"
           });

           Myitems.Add(new Props
           {
               Myitems.items = "Hennessy",
               Myitems.number = "564 cartons",
               Myitems.price = "$3745 per carton"
           });

           Myitems.Add(new Props
           {
               Myitems.items = "Remy",
               Myitems.number = "152 cartons",
               Myitems.price = "$4987 per carton"
           });

           Myitems.Add(new Props
           {
               Myitems.items = "Red Moscato",
               Myitems.number = "765 cartons",
               Myitems.price = "$211 per carton"
           });

           Myitems.Add(new Props
           {
               Myitems.items = "E&J VSOP",
               Myitems.number = "900 cartons",
               Myitems.price = "$179 per carton"
           });

           Myitems.Add(new Props
           {
               Myitems.items = "Johnnie Walker Blue label",
               Myitems.number = "72 cartons",
               Myitems.price = "$5045 per carton"
           });

           Myitems.Add(new Props
           {
               Myitems.items = "Jameson",
               Myitems.number = "432 cartons",
               Myitems.price = "$3029 per carton"
           });

           Myitems.Add(new Props
           {
               Myitems.items = "Hennessy VSOP",
               Myitems.number = "200 cartons",
               Myitems.price = "$4856 per carton"
           });
        
            

           foreach (var item in Myitems)
           {
               //Console.WriteLine(item.items);

               //Console.WriteLine(item.number);
               Console.WriteLine(Myitems);
               Console.WriteLine("===============================");
           }
        }
       class Props
        {
            public string items{get;  set;}
            public string number {get;  set;}
            public string price {get; set;}

        }
    }

}
