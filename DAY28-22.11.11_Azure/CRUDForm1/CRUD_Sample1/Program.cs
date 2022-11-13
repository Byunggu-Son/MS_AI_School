using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Data.SqlClient; //새로 추가한 namespace는 한줄 띄워주는게 관례. data.치면 나오는게  provider들이다.
using System.Data;

namespace CRUD_Sample1
{
    internal class Program
    {
        private const string ConnectionString = "";
        
        static void Main(string[] args)
        {
            SqlConnection con = new SqlConnection(ConnectionString); //위에 namespace에서 써줬기에 괄호는 생략가능 (System.Data.SqlClient.)SqlConnection
            SqlCommand cmd = con.CreateCommand(); // command객체는 connection객체에 종속적이다.
            IDataReader reader = null;
            string query = "SELECT * FROM production.brands Where brand_id > @id"; //(sql inject 취약을 보완하기 위해)
            cmd.CommandText = query;
            cmd.Parameters.Add(new SqlParameter("@id", SqlDbType.Int)).Value = 5;

            con.Open();
            Console.WriteLine("Database Connected!");
            reader = cmd.ExecuteReader();

            while(reader.Read()) //reader객체에서 .Read()명령을 사용하면 데이터 쭉 읽음. 반복문은 끝까지 읽어주기 위함
            {
                Console.WriteLine("{0} - {1}", reader.GetInt32(0), reader.GetString(1)); //format과 비슷하지만 더 편하다. 읽은 값을 출력하고 싶다면 여기선 .GetInt32(0)
            }

            con.Close(); //자원 낭비가 심하기에 다 썼으면 close필수

            Console.ReadLine(); // 바로 꺼지면 안되니, 엔터키를 눌러 종료할 수 있게 한다.
        }
    }
}
