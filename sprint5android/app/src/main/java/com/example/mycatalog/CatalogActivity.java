    package com.example.mycatalog;

    import android.content.Intent;
    import android.os.Bundle;
    import android.widget.Button;

    import androidx.activity.EdgeToEdge;
    import androidx.appcompat.app.AppCompatActivity;
    import androidx.core.graphics.Insets;
    import androidx.core.view.ViewCompat;
    import androidx.core.view.WindowInsetsCompat;

    public class CatalogActivity extends AppCompatActivity {

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            EdgeToEdge.enable(this);
            setContentView(R.layout.activity_catalog);
            ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
                Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
                v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
                return insets;
            });
            Button botonNavegar = findViewById(R.id.boton_navegar);
            botonNavegar.setOnClickListener(v -> {
                Intent intent = new Intent(CatalogActivity.this, DetailActivity.class);
                startActivity(intent);
            });
        }
    }