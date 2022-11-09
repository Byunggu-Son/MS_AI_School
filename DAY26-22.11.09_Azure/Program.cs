using Microsoft.Azure.Devices.Client;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Timers;
using Microsoft.Azure.Devices.Client;
using Newtonsoft;
using System.Net.Mail;

namespace IoTClient
{
    internal class Program
    {
        private static System.Timers.Timer SensorTimer;
        private const string DeviceConnectionString = "HostName=labuser18iot.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=mvECjbG19LRBEn0XSxj1H1HE1ZQcynx3Aqp6o0ES3lk=";
        private const string DeviceID = "Device1";
        private static DeviceClient SensorDevice = null;

        private static DummySensor DummySensor = new DummySensor();
        static void Main(string[] args)
        {
            SetTimer();

            SensorDevice = DeviceClient.CreateFromConnectionString(DeviceConnectionString, DeviceID); //"DEvice1"은 DeviceID에 이미 저장해놨으니.

            if(SensorDevice == null)
            {
                Console.WriteLine("Failed to create DeviceClient!");
                SensorTimer.Stop();
            }


            Console.WriteLine("\nPress Enter Key to exit the application...\n");
            Console.WriteLine("The application started at {0:HH:mm:ss.fff}", DateTime.Now);
            Console.ReadLine();
            SensorTimer.Stop();
            SensorTimer.Dispose();  //메모리에서 사라지라는 뜻. 죽을 거라서 딱지를 붙여놓는 것. 돌아가다가 딱지 붙은 놈부터 죽여줌.
        }
        
        private static void SetTimer()
        {
            SensorTimer = new System.Timers.Timer(2000); // 컴퓨터는 1000분의 1초이므로 이건 2초
            SensorTimer.Elapsed += SensorTimer_Elapsed;
            SensorTimer.AutoReset = true;
            SensorTimer.Enabled = true;
        }

        private static async void SensorTimer_Elapsed(object sender, System.Timers.ElapsedEventArgs e)
        {
            Console.WriteLine("The Elapsed event was raised at{0:HH:mm:ss.fff}", e.SignalTime); // 위에서 받은 이벤트 시간
            await SendEvent();
            await ReceiveCommands(); //명령한게 있는지 체크
        }

        private static async Task SendEvent()
        {
            WeatherModel model = DummySensor.GetWeatherModel("DeviceID");

            string json = Newtonsoft.Json.JsonConvert.SerializeObject(model);
            
            Console.WriteLine(json);

            Message message = new Message(Encoding.UTF8.GetBytes(json));
            await SensorDevice.SendEventAsync(message);
        }
        static async Task ReceiveCommands() //클라우드 쪽에서 보내는 메세지를 체크
        {
            Message receivedMessage;
            string messageData;

            receivedMessage = await SensorDevice.ReceiveAsync(TimeSpan.FromSeconds(1)); //물어본게 있는지, 있다면 receivedMessage에 담음

            if (receivedMessage != null)
            {
                messageData = Encoding.ASCII.GetString(receivedMessage.GetBytes());
                Console.WriteLine("\t{0}> Received message: {1}", DateTime.Now.ToLocalTime(), messageData);

                await SensorDevice.CompleteAsync(receivedMessage);
            }
        }
    }
}
// shift + ctrl + B를 누르면 그때그때 어느 부분이 틀렸는지 잘 맞는지 확인 가능(수시로 확인)