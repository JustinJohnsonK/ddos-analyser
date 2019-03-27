# ddos-analyser

# How to - 

activate environment >> source ddos-venv/bin/activate

ensure that tshark is runnung in the background and packet details are written to the file "app/packets.csv".

terminal command to run tshark >> sudo tshark -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -E header=y -E separator='\\' -E quote=d -E occurrence=f > packets.csv

run the app >> flask run

# Options

Enabling Debug Mode >> export FLASK_DEBUG=1
