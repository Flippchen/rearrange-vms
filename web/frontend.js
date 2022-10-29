
    function get_data() {
        var path_number = document.getElementById('auswahl_datei');
        path = path_number.selectedOptions[0].text;
        var hosts = document.getElementById('Hosts').value;
        var hostsize = document.getElementById('HostSize').value;
        var auslastung = document.getElementById('Auslastung').value;
        console.log(path);
        console.log(hosts);
        console.log(hostsize);
        console.log(auslastung);
        send_data(path, hosts, hostsize, auslastung);
    }
    function send_data(path, hosts, hostsize, utilization) {
        console.log("send_data");
        eel.run_rearrange_vms(path, hosts, hostsize, utilization)((files) => {
            'use strict';
            console.log(files);
            // Delete old table
            var tables = document.getElementsByTagName("table");
            for (var i = tables.length - 1; i >= 0; i -= 1)
                if (tables[i]) tables[i].parentNode.removeChild(tables[i]);
            // Create new table
            var body = document.getElementsByTagName('body')[0];
            // Logic for table creation
            for (const [key, value] of Object.entries(files)) {
                const tbl = document.createElement('table');
                tbl.className = 'styled-table';
                const caption = tbl.createCaption()
                if ((key !== 'status') && (key !== 'total_ram_consumption')) {

                    caption.textContent = 'Host %d'.replace('%d', key);
                    var tablehead = document.createElement('thead');
                    var headrow = document.createElement('tr');
                    var tablebody = document.createElement('tbody');
                    var bodyrow = document.createElement('tr');
                    for (const [key2, value2] of Object.entries(value)) {
                        var headcell = document.createElement('th');
                        headcell.textContent = key2;
                        headrow.appendChild(headcell);
                        tablehead.appendChild(headrow);
                        tbl.appendChild(tablehead);
                        var bodycell = document.createElement('td');
                        bodycell.textContent = value2;
                        bodyrow.appendChild(bodycell);
                    }
                } else {
                    caption.textContent = key;
                    var tablebody = document.createElement('tbody');
                    var bodyrow = document.createElement('tr');
                    var bodycell = document.createElement('td');
                    bodycell.textContent = value;
                    bodyrow.appendChild(bodycell)
                }
                tablebody.appendChild(bodyrow);
                tbl.appendChild(tablebody);
                body.appendChild(tbl);
            }
        });
    }
