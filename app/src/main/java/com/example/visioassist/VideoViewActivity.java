package com.example.visioassist;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import androidx.appcompat.app.AppCompatActivity;

public class VideoViewActivity extends AppCompatActivity {

    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_video_view);

        // Initialize the WebView
        webView = findViewById(R.id.webView);
        WebSettings webSettings = webView.getSettings();

        // Enable JavaScript if needed
        webSettings.setJavaScriptEnabled(true);

        // Set a WebViewClient to handle page navigation within the WebView
        webView.setWebViewClient(new WebViewClient());

        // Load the video URL in the WebView
        String videoUrl = "http://192.168.186.160:8080/video"; // Replace with your video URL
        webView.loadUrl(videoUrl);
    }
}
