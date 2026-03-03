<?php

spl_autoload_register(function ($class) {
    include $class . '.php';
});

while (true) {

    echo PHP_EOL . "=== BUAT BUS BARU ===" . PHP_EOL;
    echo "Masukkan kapasitas bus: ";
    $kapasitas = (int) trim(fgets(STDIN));

    $bus = new Bus();
    $bus->setKapasitas($kapasitas);

    while (true) {

        echo PHP_EOL;
        echo "===== MENU BUS =====" . PHP_EOL;
        echo "1. Tambah Penumpang" . PHP_EOL;
        echo "2. Kurangi Penumpang" . PHP_EOL;
        echo "3. Cek Jumlah Penumpang" . PHP_EOL;
        echo "4. Berangkat" . PHP_EOL;
        echo "5. Keluar" . PHP_EOL;
        echo "Pilih menu: ";

        $pilih = trim(fgets(STDIN));

        switch ($pilih) {

            case 1:
                echo PHP_EOL . "Jumlah Penumpang Naik: ";
                $jumlah = (int) trim(fgets(STDIN));
                $bus->tambahPenumpang($jumlah);
                break;

            case 2:
                echo PHP_EOL . "Jumlah Penumpang Turun: ";
                $jumlah = (int) trim(fgets(STDIN));
                $bus->kurangiPenumpang($jumlah);
                break;

            case 3:
                echo PHP_EOL . "Penumpang Saat Ini: " . $bus->getJumlahPenumpang() . PHP_EOL;
                echo "Kapasitas Bus: " . $bus->getKapasitas() . PHP_EOL;
                break;

            case 4:
                echo PHP_EOL . "Bus Berangkat -->" . PHP_EOL;
                echo "Beralih ke Bus Baru..." . PHP_EOL;
                continue 3; // keluar dari 2 loop ke atas (buat bus baru)

            case 5:
                echo "Program Selesai" . PHP_EOL;
                exit;

            default:
                echo "Pilihan Salah" . PHP_EOL;
        }
    }
}