package com.project.shapedraw;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.Point;
import android.graphics.drawable.BitmapDrawable;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class ShapeDrawer extends AppCompatActivity {
    private static final String TAG ="3";
    String shape;
    String color;
    String filled;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shape_drawer);
        Button back=findViewById(R.id.back);
        Intent intent=getIntent();
        shape=intent.getStringExtra("shape");
        color=intent.getStringExtra("color");
        filled=intent.getStringExtra("filled");
        Log.d(TAG, "onCreate: "+shape+"  "+color);
        Bitmap bg = Bitmap.createBitmap(720, 1280, Bitmap.Config.ARGB_8888);

        ImageView i = findViewById(R.id.imageView);
        i.setBackground(new BitmapDrawable(this.getResources(),bg));

        Canvas canvas = new Canvas(bg);
        Paint paint= new Paint();
        if(filled.equals("true"))
            paint.setStyle(Paint.Style.FILL);
        else if(filled.equals("false"))
            paint.setStyle(Paint.Style.STROKE);
        if(color.equals("Red"))
            paint.setColor(Color.RED);
        if(color.equals("Blue"))
            paint.setColor(Color.BLUE);
        if(color.equals("Green"))
            paint.setColor(Color.GREEN);



        if(shape.equals("Rectangle"))
            canvas.drawRect(100, 400, 650, 700, paint);
        if(shape.equals("Circle"))
            canvas.drawCircle(400, 450, 150, paint);
        if(shape.equals("Oval"))
            canvas.drawOval(200, 300, 650, 700, paint);
        if(shape.equals("Triangle")) {
            Point a = new Point(0, 0);
            Point b = new Point(0, 100);
            Point c = new Point(87, 50);

            Path path = new Path();
            path.setFillType(Path.FillType.EVEN_ODD);
            path.lineTo(b.x, b.y);
            path.lineTo(c.x, c.y);
            path.lineTo(a.x, a.y);
            path.close();

            canvas.drawPath(path, paint);
        }
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(ShapeDrawer.this,MainActivity.class);
                startActivity(intent);
            }
        });
    }
}
