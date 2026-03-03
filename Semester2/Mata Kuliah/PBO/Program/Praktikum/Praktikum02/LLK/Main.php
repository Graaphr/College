<?php

// Mencari Hitung.php
// Lebih tepatnya mencari class yang dibutuhkan langsung dalam folder yang ditempati
spl_autoload_register(function ($class) {
    include $class . '.php';
});

// Buat objek dengan nama hitung
$hitung = new Hitung();

echo "=============================" . PHP_EOL;
echo "        MENU PROGRAM         " . PHP_EOL;
echo "=============================" . PHP_EOL;
echo "1. Hitung Luas Lingkaran" . PHP_EOL;
echo "2. Hitung Kecepatan" . PHP_EOL;
echo "Pilih menu (1/2): ";

// Input pilihan pengguna
$pilihan = trim(fgets(STDIN));

echo PHP_EOL;

// Ubah sesuai dengan input pilihan pengguna
switch ($pilihan) {

// Luas Lingkaran
    case 1:
        echo "=== HITUNG LUAS LINGKARAN ===" . PHP_EOL;
        echo "Masukkan jari-jari: ";
        $hitung->jariJari = trim(fgets(STDIN));

        // Ambil Fungsi dari hitung.php
        echo "Luas Lingkaran: " . $hitung->getLuasLingkaran() . PHP_EOL;
        break;

// Kecepatan
    case 2:
        echo "=== HITUNG KECEPATAN ===" . PHP_EOL;
        echo "Masukkan jarak (s): ";
        $hitung->jarak = trim(fgets(STDIN));

        echo "Masukkan waktu (t): ";
        $hitung->waktu = trim(fgets(STDIN));

        // Ambil Fungsi dari hitung.php
        echo "Kecepatan (v): " . $hitung->getKecepatan() . PHP_EOL;
        break;

// Selain Input 1 dan 2
    default:
        echo "Pilihan tidak valid!" . PHP_EOL;
}