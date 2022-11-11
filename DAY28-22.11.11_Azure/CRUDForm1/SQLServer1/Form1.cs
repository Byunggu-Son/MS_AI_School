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
using System.Collections;

namespace SQLServer1
{
    public partial class frmMain : Form
    {
        // 연결에 필요한 객체들을 선언함
        private const string CONNECTION_STRING = "S"; //상수(바꿀수없음)는 대문자로 쓰는게 관례
        private SqlConnection SqlCon = null;
        private SqlCommand SqlCmd = null;
        private SqlDataAdapter SqlApt = new SqlDataAdapter();

        private DataSet dataMain = new DataSet();

        public frmMain()
        {
            InitializeComponent();
        }

        private void btnConnect_Click(object sender, EventArgs e)
        {
            SqlCon = new SqlConnection(CONNECTION_STRING); //SQL DB연결. 이전과 달리 위에 멤버변수를 따로 정의해서 쓰는 이유는 클릭되는 순간 연결되게 하기 위함
            btnConnect.Enabled = false; //연결이 되고 나면 이 버튼은 사용할 수 없는 상태가 됨.
        }

        private void btnGetData_Click(object sender, EventArgs e)
        {
            string query = "SELECT * FROM production.brands";
            SqlCommand cmd = SqlCon.CreateCommand(); //위에 쓴 Sqlcon을 불러와서 필요할 때만 쓰는 것도 방법(스케일이 커질수록 효율적)
            cmd.CommandText = query;

            SqlApt.SelectCommand = cmd;
            SqlApt.Fill(dataMain); //Fill로 채워지게 되면 null이 아닌 Dataset객체가 된다. cmd객체 쓰면 꼭 닫아줘야하지만 adapter객체는 fill메소드를  쓰면 지가 스스로 닫아줌.
            // break point를 걸어 어디서 오류났는지 짐작(break point: 맨 앞 클릭>>빨간원 생성)

            lstBrends.Items.Clear(); // 불러올 때마다 이전에 불러온 항목들이 밑에 쌓이므로 clear는 꼭 써줘야 한다.

            DataRowCollection dataRows = dataMain.Tables[0].Rows;//ADO.NET구조 dataset/collection그림보며 이해하기. 첫번째 테이블의 row들을 가져오는 것.(첫 번째 테이블을 이루는 row를 가져온다는 뜻)

            // data 가져오기
            for(int i = 0; i < dataRows.Count; i++)
            {
                lstBrends.Items.Add(dataRows[i][1].ToString()); //[1]번인 이유는 row[0]은 id/name이니깐!
            }

            //Fill to DataGridView
            DataSet dataProducts = new DataSet();
            query = "SELECT * FROM production.brands"; //가지고 오는 쿼리가 달라져야되니깐 선언
            cmd.CommandText = query;
            SqlApt.Fill(dataProducts);
            grdProducts.DataSource = dataProducts.Tables[0]; //첫번째 테이블에 있는 내용을 바인딩

            btnGetData.Enabled = false;

        }

        private void lstBrends_SelectedIndexChanged(object sender, EventArgs e) // 알아두자! EventArgs e : 이벤트가 발생될때 나한테 돌려주고 싶은 값
        {
            if(lstBrends.SelectedIndex == -1) //선택이 되어 있지 않은 상태이다. 선택된 상태는 0이며 return됨
            {
                return;
            }
            //Fill to DataGridView -> item select 하면 해당되는 brend를 gridlistbox에 나타나게 함
            // 선택한 인덱스에 대한 값을 가져옴.
            int selectedIndex = lstBrends.SelectedIndex; //-1이 아닌 무엇인가 선택된 상태
            int selectedBrandId = Int32.Parse(dataMain.Tables[0].Rows[selectedIndex][0].ToString()); // 리스트박스 안에 있는 selectedIndex와 Table의 인덱스가 일치한다. 그러므로 selectedIndex의 첫 번째 항목을 가져오면 brand_id가 된다.(0 대신 1을 쓰면 brand_name을 가져옴)
            //row객체 안에 들어가 있는건 기본적으로 오브젝트 타입. 필요한 형태대로 converting해줘야됨. parse는 문자만 인식(ToString)


            DataSet dataProducts = new DataSet();
            string query = "SELECT * FROM production.products WHERE brand_id = @brand_id";
            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.Parameters.Add(new SqlParameter("@brand_id", SqlDbType.Int)).Value = selectedBrandId;
            cmd.CommandText = query;
            SqlApt.SelectCommand = cmd;
            SqlApt.Fill(dataProducts);
            grdProducts.DataSource = dataProducts.Tables[0]; //앞서 말했듯 2번째 방법으로 데이터 셋의 첫번째 테이블과 바인딩해서 가져옴.
        }

        private void btnVIPmembers_Click(object sender, EventArgs e)
        {
            frmVIPMembers vip = new frmVIPMembers();
            vip.ShowDialog(); // show는 단순히 새 창을 열고 창 이동이 가능(알트탭같은 느낌). showDialog는 창 컨트롤 불가. 일반적으로는 ShowDialog을 많이 사용
        }
    }
}
