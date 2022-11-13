using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data.SqlClient;
using System.Configuration;

namespace SQLServer1
{
    public partial class frmVIPMembers : Form
    {
        private string connection_string = "";
        private SqlConnection SqlCon = null;// 전역변수를 쓰면 이걸 매번 안 써도 됨.
        private SqlCommand SqlCmd = null;
        private SqlDataAdapter SqlApt = new SqlDataAdapter();

        private DataSet dataMain = new DataSet();

        public frmVIPMembers()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        //업데이트와 삭제
        private void frmVIPMembers_Load(object sender, EventArgs e)
        {
            connection_string = ConfigurationManager.AppSettings["connection_string"];
            ReloadData();
        }

        public void ReloadData()
        {
            dataMain.Clear();

            SqlCon = new SqlConnection(connection_string);

            string query = "SELECT * FROM dbo.VIPmembers";
            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.CommandText = query;

            SqlApt.SelectCommand = cmd;
            SqlApt.Fill(dataMain);

            grdMemberList.DataSource = dataMain.Tables[0];
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            frmVIPMembersInput vipInput = new frmVIPMembersInput(this); //인스턴스는 만들어질때마다 주소가 달라지므로, 주소를 주며 그 안의 것들을 가져올 수 있게 함.
            vipInput.ShowDialog();
        }


    }
}
