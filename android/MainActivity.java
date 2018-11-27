package com.example.saima.vit_ap_assist_admin;

import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.AsyncTask;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.ByteArrayOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;


public class MainActivity extends AppCompatActivity  {
    public static final int CAMERA_REQUEST = 9999;
    Button login;
    ImageView iv;
    Boolean check_image = false;
    String image;
    String person="";
    TextView textView14 = (TextView)findViewById(R.id.textView14);




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        login = (Button)findViewById(R.id.button);
        iv = (ImageView)findViewById(R.id.imageView);




    }
    public void open(View view){
       textView14.setText(person);


    }
    public void login(View view){
        //Intent intent = new Intent(getApplicationContext(), Home.class);
        //startActivity(intent);


            Intent intent1 = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
            startActivityForResult(intent1, CAMERA_REQUEST);


    }
    public static String ConvertBitmapToString(Bitmap bitmap){
        String encodedImage = "";

        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        bitmap.compress(Bitmap.CompressFormat.JPEG, 100, byteArrayOutputStream);
        try {
            encodedImage= Base64.encodeToString(byteArrayOutputStream.toByteArray(), Base64.DEFAULT);
        } catch (Exception e) {
            e.printStackTrace();
        }

        return encodedImage;
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
       if(requestCode==CAMERA_REQUEST)
       {
           Bitmap bitmap = (Bitmap)data.getExtras().get("data");
           iv.setImageBitmap(bitmap);
           Bitmap resizedBitmap = Bitmap.createScaledBitmap(bitmap, 1000, 458, false);
           image = ConvertBitmapToString(resizedBitmap);

           DownloadTask task = new DownloadTask();

           task.execute(" https://bc8ed974.ngrok.io/hackathon/android/test");



       }

    }





    public class DownloadTask extends AsyncTask<String , Void , String> {
        String data="";
        String Content;
        BufferedReader reader;

        protected void onPreExecute() {



            try {

                //data += "&" + URLEncoder.encode("image", "UTF-8") + "=" + "data:image/png;base64," + image;
                data = image;

            } catch (Exception e) {
                e.printStackTrace();
            }

        }

        @Override
        protected String doInBackground(String... urls) {



            String result = "";
            URL url;
            HttpURLConnection urlConnection = null;

            try {
                url = new URL(urls[0]);

                urlConnection = (HttpURLConnection) url.openConnection();

                urlConnection.setDoInput(true);
                urlConnection.setDoInput(true);
                urlConnection.setRequestMethod("POST");
                urlConnection.setDoOutput(true);
                urlConnection.setRequestProperty("Content-Length", "" + data.getBytes().length);
                urlConnection.setRequestProperty("Connection", "Keep-Alive");


                urlConnection.connect();

                OutputStream output = urlConnection.getOutputStream();
                BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(output, "UTF-8"));



                //bitmap.compress(Bitmap.CompressFormat.JPEG, 50, output);
                writer.write(data);
                writer.flush();
                writer.close();

                reader = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
               
                StringBuilder sb = new StringBuilder();
                String line = null;
                while ((line = reader.readLine()) != null) {
                    sb.append(line);
                }

                Content = sb.toString();
                return Content;







            } catch (Exception e) {
                e.printStackTrace();

            }


            return "not found";
        }
        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);
            Toast.makeText(getApplicationContext() ,"Welcome: " +result+" To the API Template demo app " , Toast.LENGTH_LONG).show();
            person = result;


            if(result=="not found"){
                Toast.makeText(MainActivity.this, "Invalid Entry", Toast.LENGTH_SHORT).show();

            }

        }


    }
}
