<?php
class Mahasiswa {
    public $nama;
    public $nim;

    public function __construct($nama, $nim) {
        $this->nama = $nama;
        $this->nim = $nim;
    }

    // Ini Fungsinya
    public function tampilData() {
        echo "Nama: " . $this->nama . PHP_EOL;
        echo "NIM: " . $this->nim . PHP_EOL;
    }
}

// Meminta input dari pengguna
$nama = readline("Masukkan Nama: ");
$nim = readline("Masukkan NIM: ");

// Kita buat objeknya
$mhs1 = new Mahasiswa($nama, $nim);

// Lalu kita tampilkan datanya
echo PHP_EOL . "=== Data Mahasiswa ===" . PHP_EOL;
$mhs1->tampilData();
?>