package com.project.shapedraw;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.Spinner;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    Spinner shapes,colors;
    RadioButton filled;
    Button submit;
    String[] Shapes={"Circle","Oval","Rectangle","Triangle"};
    String[] Colors={"Red","Blue","Green"};
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        shapes=findViewById(R.id.shapemenu);
        colors=findViewById(R.id.colormenu);
        filled=findViewById(R.id.filled);
        submit=findViewById(R.id.submit);

        ArrayAdapter adapter= new ArrayAdapter(MainActivity.this,android.R.layout.simple_spinner_item,Shapes);
        shapes.setAdapter(adapter);

        ArrayAdapter adapter1= new ArrayAdapter(MainActivity.this,android.R.layout.simple_spinner_item,Colors);
        colors.setAdapter(adapter1);



        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String Sobject = shapes.getSelectedItem().toString();
                String Cobject = colors.getSelectedItem().toString();
                boolean fillstate = filled.isChecked();
                String filltext = String.valueOf(fillstate);
                Intent intent=new Intent(MainActivity.this,ShapeDrawer.class);
                intent.putExtra("shape",Sobject);
                intent.putExtra("color",Cobject);
                intent.putExtra("filled",filltext);
                startActivity(intent);
            }
        });
    }
}
