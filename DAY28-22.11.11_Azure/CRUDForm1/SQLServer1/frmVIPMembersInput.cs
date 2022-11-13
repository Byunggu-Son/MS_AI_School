using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms; //이것들이 다 하나의 파일이라고 생각.

using System.Configuration;
using System.Data.SqlClient;

namespace SQLServer1
{
    public partial class frmVIPMembersInput : Form
    {
        private string CONNECTION_STRING;
        private frmVIPMembers frm_vip_members;

        public frmVIPMembersInput(frmVIPMembers vipmembers)
        {
            InitializeComponent();

            frm_vip_members = vipmembers;
        }

        private void btnOk_Click(object sender, EventArgs e)
        {
            if(txtName.Text.Trim().Length == 0) //VIP의 name/phone/email 중 name은 꼭 들어가야된다는 가정 하에. trim으로 공백제거하고 안의 입력값으로 입력여부 확인
            {
                MessageBox.Show("Please input VIP name!",
                    "ERROR",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
            }

            CONNECTION_STRING = ConfigurationManager.AppSettings["connection_string"]; // References에서 해당 어셈블리 추가(system Configuration) 후 App.config의 세팅값을 받기 위함

            string query = "INSERT INTO dbo.VIPmembers(member_name, member_email, member_phone) VALUES(@name, @email, @phone)";//파라메터가 알아서 ''를 붙여주기에 sql inject도 피해갈 수 있다.

            SqlConnection con = new SqlConnection(CONNECTION_STRING);
            SqlCommand cmd = con.CreateCommand();
            cmd.CommandText = query;
            cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.VarChar, 200)).Value = txtName.Text;
            cmd.Parameters.Add(new SqlParameter("@email", SqlDbType.VarChar, 100)).Value = txtEmail.Text;
            cmd.Parameters.Add(new SqlParameter("@phone", SqlDbType.VarChar, 25)).Value = txtPhone.Text;

            con.Open();
            cmd.ExecuteNonQuery();//명령을 수행하고 영향을 받은 행의 수를 반환하는 메서드
            con.Close();

            frm_vip_members.ReloadData();

            this.Close();

            
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            if(txtName.Text.Trim().Length != 0)// 입력된 항목이 있는데 닫으려고 한다면 재확인해주는 작업
            {
                 var buttonResult = MessageBox.Show("Close right now?", "Close", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
                if(buttonResult == DialogResult.No)
                {
                    return;
                }
            }
            this.Close(); 
        }
    }
}
