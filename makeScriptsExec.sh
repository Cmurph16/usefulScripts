for i in passgen.py 
do
    cp $i /usr/local/bin/${i%.*}
    chmod +x /usr/local/bin/${i%.*}
done