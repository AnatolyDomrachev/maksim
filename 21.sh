num=10000

date > time.txt
for((i=0;i<$num;i++))
    do
        bash 22.sh &
	sleep 0.002
    done

date >> time.txt
