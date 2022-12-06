using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CZU_TaskAssign
{
    internal class Task
    {
        public string title { get; set; }
        public string description { get; set; }
        public string assigned_to { get; set; }
        public string status { get; set; }
        public Nullable<System.DateTime> created_at { get; set; }
        public Nullable<System.DateTime> updated_at { get; set; }
    }
}
