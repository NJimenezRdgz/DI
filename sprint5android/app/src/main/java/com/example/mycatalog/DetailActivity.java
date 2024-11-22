package com.example.mycatalog;

import android.content.res.Configuration;
import android.os.Bundle;
import android.widget.ImageView;
import com.bumptech.glide.Glide;
import com.bumptech.glide.request.RequestOptions;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.time.Instant;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_detail);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        ImageView imageView = findViewById(R.id.detail_imagen_circular);
        int orientation = getResources().getConfiguration().orientation;

// si es horizontal cambiar el layout a "detail_activity.xml".
        if (orientation == Configuration.ORIENTATION_LANDSCAPE)
            setContentView(R.layout.detail_activity);
        else
            // si es vertical usar "activity_detail.xml".
            setContentView(R.layout.activity_detail);

        Glide.with(this)
                .load("https://example.com/image.jpg")
                .apply(RequestOptions.circleCropTransform()) // Recorta en círculo
                .placeholder(R.drawable.placeholder)
                .into(imageView);
    }
}