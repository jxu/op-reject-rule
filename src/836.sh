wget -q -O - https://projecteuler.net/minimal=836 | 
    pup b text{} | 
    sed -E 's/(\b[a-z])\w*/\1/g' | tr -d "[:space:]"

