while read filename; do
    convert ${filename} ${filename%ppm}gif
    printf ·
done
echo ✅
