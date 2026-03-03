<?php

spl_autoload_register(function ($class) {
    include $class . '.php';
});

$bd1 = new BangunDatar();

// Mengubah nilai di property
$bd1->panjang = 10;
$bd1->lebar = 5;
$luasBd1 = $bd1->getLuas();
echo "=== Menggunakan Pre-Determined Attribute/Property ===", PHP_EOL;
echo "Panjang Bangun Datar: " . $bd1->panjang, PHP_EOL;
echo "Lebar Bangun Datar: " . $bd1->lebar, PHP_EOL;
echo "Luas Bangun Datar: " . $luasBd1, PHP_EOL;

// Membuat objek baru dengan nama bd2
$bd2 = new BangunDatar();

// Contoh input dari user
echo PHP_EOL . "=== Menggunakan Inputted Attribute/Property ===", PHP_EOL;
echo "Masukkan Panjang Bangun Datar: ";
$bd2->panjang = trim(fgets(STDIN));

echo "Masukkan Lebar Bangun Datar: ";
$bd2->lebar = trim(fgets(STDIN));

echo "Luas Bangun Datar: ", $bd2->getLuas(), PHP_EOL;