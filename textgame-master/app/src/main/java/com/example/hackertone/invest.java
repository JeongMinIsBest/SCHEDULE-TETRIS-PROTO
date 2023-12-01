package com.example.hackertone;

import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class invest extends AppCompatActivity {
    TextView inputText, outputText;
    Button backBtn;
    public invest() {
        inputText = findViewById(R.id.inputText);
        outputText = findViewById(R.id.outputText);
        backBtn = findViewById(R.id.backBtn);

        backBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });
    }
}
