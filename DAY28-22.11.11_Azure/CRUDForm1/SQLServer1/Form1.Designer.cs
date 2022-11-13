namespace SQLServer1
{
    partial class frmMain
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
            this.btnConnect = new System.Windows.Forms.Button();
            this.btnGetData = new System.Windows.Forms.Button();
            this.lstBrends = new System.Windows.Forms.ListBox();
            this.grdProducts = new System.Windows.Forms.DataGridView();
            this.btnVIPmembers = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.grdProducts)).BeginInit();
            this.SuspendLayout();
            // 
            // btnConnect
            // 
            this.btnConnect.Location = new System.Drawing.Point(52, 48);
            this.btnConnect.Name = "btnConnect";
            this.btnConnect.Size = new System.Drawing.Size(102, 30);
            this.btnConnect.TabIndex = 0;
            this.btnConnect.Text = "Connect";
            this.btnConnect.UseVisualStyleBackColor = true;
            this.btnConnect.Click += new System.EventHandler(this.btnConnect_Click);
            // 
            // btnGetData
            // 
            this.btnGetData.Location = new System.Drawing.Point(50, 84);
            this.btnGetData.Name = "btnGetData";
            this.btnGetData.Size = new System.Drawing.Size(102, 23);
            this.btnGetData.TabIndex = 1;
            this.btnGetData.Text = "GetData";
            this.btnGetData.UseVisualStyleBackColor = true;
            this.btnGetData.Click += new System.EventHandler(this.btnGetData_Click);
            // 
            // lstBrends
            // 
            this.lstBrends.FormattingEnabled = true;
            this.lstBrends.Location = new System.Drawing.Point(181, 48);
            this.lstBrends.Name = "lstBrends";
            this.lstBrends.Size = new System.Drawing.Size(120, 95);
            this.lstBrends.TabIndex = 2;
            this.lstBrends.SelectedIndexChanged += new System.EventHandler(this.lstBrends_SelectedIndexChanged);
            // 
            // grdProducts
            // 
            this.grdProducts.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.grdProducts.Location = new System.Drawing.Point(347, 48);
            this.grdProducts.Name = "grdProducts";
            this.grdProducts.RowHeadersWidth = 51;
            this.grdProducts.Size = new System.Drawing.Size(414, 372);
            this.grdProducts.TabIndex = 3;
            // 
            // btnVIPmembers
            // 
            this.btnVIPmembers.Location = new System.Drawing.Point(52, 160);
            this.btnVIPmembers.Name = "btnVIPmembers";
            this.btnVIPmembers.Size = new System.Drawing.Size(183, 23);
            this.btnVIPmembers.TabIndex = 4;
            this.btnVIPmembers.Text = "VIP Management";
            this.btnVIPmembers.UseVisualStyleBackColor = true;
            this.btnVIPmembers.Click += new System.EventHandler(this.btnVIPmembers_Click);
            // 
            // frmMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.btnVIPmembers);
            this.Controls.Add(this.grdProducts);
            this.Controls.Add(this.lstBrends);
            this.Controls.Add(this.btnGetData);
            this.Controls.Add(this.btnConnect);
            this.Name = "frmMain";
            this.Text = "Welcome to SQLServer Tester";
            ((System.ComponentModel.ISupportInitialize)(this.grdProducts)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnConnect;
        private System.Windows.Forms.Button btnGetData;
        private System.Windows.Forms.ListBox lstBrends;
        private System.Windows.Forms.DataGridView grdProducts;
        private System.Windows.Forms.Button btnVIPmembers;
    }
}

