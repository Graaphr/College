<?php

spl_autoload_register(function ($class) {
    include $class . '.php';
});

$bd1 = new BangunDatarEncapsulation();
$bd1->setPanjang(10);
$bd1->setLebar(5);
echo "Panjang Bangun Datar: " . $bd1->getPanjang(), PHP_EOL;
echo "Lebar Bangun Datar: " .$bd1->getLebar(), PHP_EOL;
echo "Luas Bangun Datar: " .$bd1->getLuas();
