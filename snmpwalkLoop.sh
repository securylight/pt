for n in $(seq 108 111); do
	for m in $(seq 248 255); do
        	snmpwalk -Os -c public -v 1 XXX.XXX.$n.$m
	done
done

