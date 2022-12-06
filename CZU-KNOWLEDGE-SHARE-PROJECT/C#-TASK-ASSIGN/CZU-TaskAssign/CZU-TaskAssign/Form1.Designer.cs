namespace CZU_TaskAssign
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.get_tasks = new System.Windows.Forms.Button();
            this.notification = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.description = new System.Windows.Forms.TextBox();
            this.assign_task = new System.Windows.Forms.Button();
            this.taskListView = new System.Windows.Forms.DataGridView();
            this.title = new System.Windows.Forms.TextBox();
            this.task_assign_notification = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.taskListView)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.label1.Location = new System.Drawing.Point(37, 89);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(46, 20);
            this.label1.TabIndex = 1;
            this.label1.Text = "Title:";
            // 
            // get_tasks
            // 
            this.get_tasks.BackColor = System.Drawing.SystemColors.MenuHighlight;
            this.get_tasks.Cursor = System.Windows.Forms.Cursors.Hand;
            this.get_tasks.Location = new System.Drawing.Point(754, 258);
            this.get_tasks.Name = "get_tasks";
            this.get_tasks.Size = new System.Drawing.Size(281, 45);
            this.get_tasks.TabIndex = 3;
            this.get_tasks.Text = "GET ALL TASKS";
            this.get_tasks.UseVisualStyleBackColor = false;
            this.get_tasks.Click += new System.EventHandler(this.get_tasks_Click);
            // 
            // notification
            // 
            this.notification.AutoSize = true;
            this.notification.Location = new System.Drawing.Point(719, 42);
            this.notification.Name = "notification";
            this.notification.Size = new System.Drawing.Size(0, 16);
            this.notification.TabIndex = 4;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.label2.Location = new System.Drawing.Point(37, 131);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(100, 20);
            this.label2.TabIndex = 5;
            this.label2.Text = "Description:";
            // 
            // description
            // 
            this.description.Location = new System.Drawing.Point(158, 129);
            this.description.Multiline = true;
            this.description.Name = "description";
            this.description.Size = new System.Drawing.Size(340, 94);
            this.description.TabIndex = 6;
            // 
            // assign_task
            // 
            this.assign_task.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.assign_task.Cursor = System.Windows.Forms.Cursors.Hand;
            this.assign_task.Location = new System.Drawing.Point(158, 239);
            this.assign_task.Name = "assign_task";
            this.assign_task.Size = new System.Drawing.Size(261, 41);
            this.assign_task.TabIndex = 7;
            this.assign_task.Text = "ASSIGN TO ADMIN";
            this.assign_task.UseVisualStyleBackColor = false;
            this.assign_task.Click += new System.EventHandler(this.assign_task_Click);
            // 
            // taskListView
            // 
            this.taskListView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.taskListView.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.taskListView.Location = new System.Drawing.Point(0, 309);
            this.taskListView.Name = "taskListView";
            this.taskListView.RowHeadersWidth = 51;
            this.taskListView.RowTemplate.Height = 24;
            this.taskListView.Size = new System.Drawing.Size(1047, 297);
            this.taskListView.TabIndex = 8;
            // 
            // title
            // 
            this.title.Location = new System.Drawing.Point(158, 76);
            this.title.Multiline = true;
            this.title.Name = "title";
            this.title.Size = new System.Drawing.Size(340, 47);
            this.title.TabIndex = 9;
            // 
            // task_assign_notification
            // 
            this.task_assign_notification.AutoSize = true;
            this.task_assign_notification.BackColor = System.Drawing.Color.Black;
            this.task_assign_notification.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F);
            this.task_assign_notification.ForeColor = System.Drawing.Color.White;
            this.task_assign_notification.Location = new System.Drawing.Point(504, 79);
            this.task_assign_notification.Name = "task_assign_notification";
            this.task_assign_notification.Size = new System.Drawing.Size(0, 18);
            this.task_assign_notification.TabIndex = 10;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1047, 606);
            this.Controls.Add(this.task_assign_notification);
            this.Controls.Add(this.title);
            this.Controls.Add(this.taskListView);
            this.Controls.Add(this.assign_task);
            this.Controls.Add(this.description);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.notification);
            this.Controls.Add(this.get_tasks);
            this.Controls.Add(this.label1);
            this.ForeColor = System.Drawing.SystemColors.InfoText;
            this.Name = "Form1";
            this.Text = "CZU TASK ASSIGN";
            ((System.ComponentModel.ISupportInitialize)(this.taskListView)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button get_tasks;
        private System.Windows.Forms.Label notification;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox description;
        private System.Windows.Forms.Button assign_task;
        private System.Windows.Forms.DataGridView taskListView;
        private System.Windows.Forms.TextBox title;
        private System.Windows.Forms.Label task_assign_notification;
    }
}

