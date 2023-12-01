package com.example.hackertone;

import androidx.appcompat.app.AppCompatActivity;

import android.content.res.Resources;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    ImageView imageView;
    TextView title, content;
    String[] episode, titles, story, contents;
    Button nextBtn;
    int titleindex = 0, contindex = 0, epiindex = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        imageView = findViewById(R.id.imageView);
        title = findViewById(R.id.title);
        content = findViewById(R.id.content);
        nextBtn = findViewById(R.id.nextBtn);

        Resources res = getResources();
        episode = res.getStringArray(R.array.episode);
        titles = res.getStringArray(R.array.titles);
        story = res.getStringArray(R.array.story);

        contents = story[0].split("\n");
        continueStory(3);

        nextBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                continueStory(1);
            }
        });
    }

    private void continueStory(int num) {
        if(num == 0) {
            title.setText(titles[titleindex]);
        }
        if(num == 1) {
            printText(contents[contindex++]);
        }
        if(num == 3) {
            title.setText(titles[titleindex]);
            printText(contents[contindex++]);
        }
    }
    int i = 0;
    private void printText(String text) {
        content.setText(text);
        //문자열 딜레이 (글자 한 글자씩 순차적으로 print)
        /*
        content.setText("");
        Handler handler = new Handler();
        String[] word = text.split("");

        for(i = 0; i < text.length() - 1; i++) {
            handler.postDelayed(new Runnable()
            { @Override public void run(){
                content.append(word[i]);
             } }, 1000);
        } */
    }
}