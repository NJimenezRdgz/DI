package com.example.mycatalog;

import android.content.Intent;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class CatalogFragment extends Fragment {


    private String mParam1;
    private String mParam2;

    public CatalogFragment() {
        // Required empty public constructor
    }
    // TODO: Rename and change types and number of parameters
    public static CatalogFragment newInstance(String param1, String param2) {
        CatalogFragment fragment = new CatalogFragment();

        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
        }

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view= inflater.inflate(R.layout.fragment_catalog,container,false);

        Button botonNavegar = view.findViewById(R.id.boton_navegar_fragment);
        botonNavegar.setOnClickListener(v -> {
            Intent intent = new Intent(requireContext(), DetailActivity.class);
            startActivity(intent);
            requireActivity().finish();
        });
        return view;
    }


}