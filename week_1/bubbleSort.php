<?php

/*
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function countSwaps($a) {
    // Write your code here
    $numberOfSwaps = 0;
    
    for ($i = 0; $i < count($a); $i++) 
    {
    
        for ($j = 0; $j < count($a) - 1; $j++) 
        {
        // Swap adjacent elements if they are in decreasing order
            if ($a[$j] > $a[$j + 1]) {
              
                $t = $a[$j];
                $a[$j] = $a[$j+1];
                $a[$j+1] = $t;
                
                $numberOfSwaps++;
        }
    }
    
}
echo "Array is sorted in ".$numberOfSwaps." swaps.\n";
echo "First Element: ".$a[0]."\n";
echo "Last Element: ".$a[(count($a)-1)]."\n";
}


$n = intval(trim(fgets(STDIN)));

$a_temp = rtrim(fgets(STDIN));

$a = array_map('intval', preg_split('/ /', $a_temp, -1, PREG_SPLIT_NO_EMPTY));

countSwaps($a);
