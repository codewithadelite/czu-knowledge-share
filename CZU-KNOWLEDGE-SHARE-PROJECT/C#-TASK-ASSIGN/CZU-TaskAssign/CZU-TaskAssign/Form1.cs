using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net.Http;
using MaterialSkin;
using MaterialSkin.Controls;
using MaterialSkin.Animations;
using Newtonsoft.Json;

namespace CZU_TaskAssign
{
    public partial class Form1 : MaterialForm
    {
        public Form1()
        {
            var materialSkinManager = MaterialSkinManager.Instance;
            materialSkinManager.AddFormToManage(this);
            materialSkinManager.Theme = MaterialSkinManager.Themes.LIGHT;
            materialSkinManager.ColorScheme = new ColorScheme(Primary.BlueGrey800, Primary.BlueGrey900, Primary.BlueGrey500, Accent.LightBlue200, TextShade.WHITE);
            InitializeComponent();
        }

        private void get_tasks_Click(object sender, EventArgs e)
        {
            //Notifying user that application is requesting data from internet 
            notification.Text = "Loading data from web";

            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri("http://czu-knowledge-share.herokuapp.com/api/v1/");

            HttpResponseMessage response = client.GetAsync("tasks/").Result;
  
            notification.Text = "";
            var task = response.Content.ReadAsStringAsync().Result;
            var result = JsonConvert.DeserializeObject<List<Task>>(task);
            taskListView.DataSource = result;


        }

        private void assign_task_Click(object sender, EventArgs e)
        {
            //Notifying user that application is sending data over internet 
            notification.Text = "Application is sending data to web application";


            TaskAssign new_task = new TaskAssign() { title = title.Text, description = description.Text };
            var json_task = JsonConvert.SerializeObject(new_task);
            var payload = new StringContent(json_task.ToString(), Encoding.UTF8, "application/json");

            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri("http://czu-knowledge-share.herokuapp.com/api/v1/");

            var response = client.PostAsync("tasks/",payload).Result.Content.ReadAsStringAsync().Result;

            if (response != "")
            {
                notification.Text = "";

                dynamic result = JsonConvert.DeserializeObject(response);
                task_assign_notification.Text = "Assigned successfully: Task is assigned to" + result.assigned_to;

                title.Text = "";
                description.Text = "";

                //Waiting 5 seconds before hiding task assign notification
                System.Threading.Thread.Sleep(5000);
                task_assign_notification.Text = "";

            }
            else
            {
                notification.Text = "There was error. Please try again.";

                //Waiting 5 seconds before hiding task assign notification
                System.Threading.Thread.Sleep(5000);
                notification.Text = "";
            }



        }
    }
}
