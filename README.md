# A76XX AT Command Implementation Checklist

Source: `documentation/datasheet/A76XX_Series_AT_Command_Manual_V1.09.pdf`

Use this checklist to track implementation status for each command in the manual.
Mark `[x]` when a command is implemented and verified.

- Sections: `34`
- Commands listed: `396`
- Unique commands: `396`

## Section Summary
- `V.25TER and Common`: 20 commands
- `Status Control`: 13 commands
- `Network`: 13 commands
- `Packet Domain`: 17 commands
- `SIM Card`: 15 commands
- `Call Control`: 22 commands
- `Phonebook`: 5 commands
- `SMS`: 22 commands
- `Serial Interface`: 11 commands
- `Hardware`: 14 commands
- `File System`: 16 commands
- `File Transmission`: 3 commands
- `Internet Service`: 3 commands
- `TCP/IP`: 23 commands
- `HTTP(S)`: 9 commands
- `FTP(S)`: 19 commands
- `MQTT(S)`: 17 commands
- `SSL`: 16 commands
- `TTS`: 3 commands
- `Audio`: 9 commands
- `FOTA`: 2 commands
- `SCFOTA`: 2 commands
- `GNSS`: 16 commands
- `WIFI`: 10 commands
- `Bluetooth`: 49 commands
- `CTBURST`: 1 commands
- `WEBSOCKET`: 5 commands
- `LWM2M`: 10 commands
- `COAP`: 8 commands
- `SMTPS`: 12 commands
- `Telecom self-registration`: 2 commands
- `PSM`: 3 commands
- `USB`: 4 commands
- `JammingDetect`: 2 commands

## V.25TER and Common (20)
- [ ] `ATD`
- [ ] `ATA`
- [ ] `ATH`
- [ ] `ATS0`
- [ ] `ATO`
- [ ] `ATI`
- [ ] `ATE`
- [ ] `AT&V`
- [ ] `ATV`
- [ ] `AT&F`
- [ ] `ATQ`
- [ ] `ATX`
- [ ] `AT&W`
- [ ] `ATZ`
- [ ] `AT+CGMI`
- [ ] `AT+CGMM`
- [ ] `AT+CGMR`
- [ ] `AT+CGSN`
- [ ] `AT+CSCS`
- [ ] `AT+GCAP`

## Status Control (13)
- [ ] `AT+CFUN`
- [ ] `AT+CSQ`
- [ ] `AT+AUTOCSQ`
- [ ] `AT+CSQDELTA`
- [ ] `AT+CPOF`
- [ ] `AT+CRESET`
- [ ] `AT+CACM`
- [ ] `AT+CAMM`
- [ ] `AT+CPUC`
- [ ] `AT+CCLK`
- [ ] `AT+CMEE`
- [ ] `AT+CPAS`
- [ ] `AT+SIMEI`

## Network (13)
- [ ] `AT+CREG`
- [ ] `AT+COPS`
- [ ] `AT+CUSD`
- [ ] `AT+CSSN`
- [ ] `AT+CPOL`
- [ ] `AT+COPN`
- [ ] `AT+CNMP`
- [ ] `AT+CNBP`
- [ ] `AT+CPSI`
- [ ] `AT+CPSITD`
- [ ] `AT+CNSMOD`
- [ ] `AT+CTZU`
- [ ] `AT+CTZR`

## Packet Domain (17)
- [ ] `AT+CGREG`
- [ ] `AT+CEREG`
- [ ] `AT+CGATT`
- [ ] `AT+CGACT`
- [ ] `AT+CGDCONT`
- [ ] `AT+CGDSCONT`
- [ ] `AT+CGTFT`
- [ ] `AT+CGQREQ`
- [ ] `AT+CGEQREQ`
- [ ] `AT+CGQMIN`
- [ ] `AT+CGEQMIN`
- [ ] `AT+CGDATA`
- [ ] `AT+CGPADDR`
- [ ] `AT+CGCLASS`
- [ ] `AT+CGEREP`
- [ ] `AT+CGAUTH`
- [ ] `AT+CPING`

## SIM Card (15)
- [ ] `AT+CICCID`
- [ ] `AT+CPIN`
- [ ] `AT+CLCK`
- [ ] `AT+CPWD`
- [ ] `AT+CIMI`
- [ ] `AT+CSIM`
- [ ] `AT+CRSM`
- [ ] `AT+SPIC`
- [ ] `AT+CSPN`
- [ ] `AT+UIMHOTSWAPON`
- [ ] `AT+UIMHOTSWAPLEVEL`
- [ ] `AT+SWITCHSIM`
- [ ] `AT+DUALSIM`
- [ ] `AT+BINDSIM`
- [ ] `AT+DUALSIMURC`

## Call Control (22)
- [ ] `AT+CVHU`
- [ ] `AT+CHUP`
- [ ] `AT+CBST`
- [ ] `AT+CRLP`
- [ ] `AT+CRC`
- [ ] `AT+CLCC`
- [ ] `AT+CEER`
- [ ] `AT+CCWA`
- [ ] `AT+CCFC`
- [ ] `AT+CLIP`
- [ ] `AT+CLIR`
- [ ] `AT+COLP`
- [ ] `AT+CHLD`
- [ ] `AT+VTS`
- [ ] `AT+VTD`
- [ ] `AT+CSTA`
- [ ] `AT+CMOD`
- [ ] `AT+VMUTE`
- [ ] `AT+CMUT`
- [ ] `AT+CSDVC`
- [ ] `AT+CMICGAIN`
- [ ] `AT+COUTGAIN`

## Phonebook (5)
- [ ] `AT+CPBS`
- [ ] `AT+CPBR`
- [ ] `AT+CPBF`
- [ ] `AT+CPBW`
- [ ] `AT+CNUM`

## SMS (22)
- [ ] `AT+CSMS`
- [ ] `AT+CPMS`
- [ ] `AT+CMGF`
- [ ] `AT+CSCA`
- [ ] `AT+CSCB`
- [ ] `AT+CSMP`
- [ ] `AT+CSDH`
- [ ] `AT+CNMA`
- [ ] `AT+CNMI`
- [ ] `AT+CGSMS`
- [ ] `AT+CMGL`
- [ ] `AT+CMGR`
- [ ] `AT+CMGS`
- [ ] `AT+CMSS`
- [ ] `AT+CMGW`
- [ ] `AT+CMGD`
- [ ] `AT+CMGMT`
- [ ] `AT+CMVP`
- [ ] `AT+CMGRD`
- [ ] `AT+CMGSEX`
- [ ] `AT+CMSSEX`
- [ ] `AT+CCONCINDEX`

## Serial Interface (11)
- [ ] `AT&D`
- [ ] `AT&C`
- [ ] `AT+IPR`
- [ ] `AT+IPREX`
- [ ] `AT+ICF`
- [ ] `AT+IFC`
- [ ] `AT+CSCLK`
- [ ] `AT+CMUX`
- [ ] `AT+CATR`
- [ ] `AT+CFGRI`
- [ ] `AT+CURCD`

## Hardware (14)
- [ ] `AT+CVALARM`
- [ ] `AT+CVAUXS`
- [ ] `AT+CVAUXV`
- [ ] `AT+CADC`
- [ ] `AT+CADC2`
- [ ] `AT+CMTE`
- [ ] `AT+CPMVT`
- [ ] `AT+CRIIC`
- [ ] `AT+CWIIC`
- [ ] `AT+CBC`
- [ ] `AT+CPMUTEMP`
- [ ] `AT+CGDRT`
- [ ] `AT+CGSETV`
- [ ] `AT+CGGETV`

## File System (16)
- [ ] `AT+FSCD`
- [ ] `AT+FSMKDIR`
- [ ] `AT+FSRMDIR`
- [ ] `AT+FSLS`
- [ ] `AT+FSDEL`
- [ ] `AT+FSRENAME`
- [ ] `AT+FSATTRI`
- [ ] `AT+FSMEM`
- [ ] `AT+FSCOPY`
- [ ] `AT+FSPRESET`
- [ ] `AT+FSOPEN`
- [ ] `AT+FSREAD`
- [ ] `AT+FSWRITE`
- [ ] `AT+FSSEEK`
- [ ] `AT+FSPOSITION`
- [ ] `AT+FSCLOSE`

## File Transmission (3)
- [ ] `AT+CFTRANRX`
- [ ] `AT+CFTRANTX`
- [ ] `AT+CFTRXBUF`

## Internet Service (3)
- [ ] `AT+CHTPSERV`
- [ ] `AT+CHTPUPDATE`
- [ ] `AT+CNTP`

## TCP/IP (23)
- [ ] `AT+NETOPEN`
- [ ] `AT+NETCLOSE`
- [ ] `AT+CIPOPEN`
- [ ] `AT+CIPSEND`
- [ ] `AT+CIPRXGET`
- [ ] `AT+CIPCLOSE`
- [ ] `AT+IPADDR`
- [ ] `AT+CIPHEAD`
- [ ] `AT+CIPSRIP`
- [ ] `AT+CIPMODE`
- [ ] `AT+CIPSENDMODE`
- [ ] `AT+CIPTIMEOUT`
- [ ] `AT+CIPCCFG`
- [ ] `AT+SERVERSTART`
- [ ] `AT+SERVERSTOP`
- [ ] `AT+CIPACK`
- [ ] `AT+CDNSGIP`
- [ ] `AT+CSOCKSETPN`
- [ ] `AT+CTCPKA`
- [ ] `AT+CDNSCFG`
- [ ] `AT+CSOC`
- [ ] `AT+CIPCFG`
- [ ] `AT+CIPSENDSTR`

## HTTP(S) (9)
- [ ] `AT+HTTPINIT`
- [ ] `AT+HTTPTERM`
- [ ] `AT+HTTPPARA`
- [ ] `AT+HTTPACTION`
- [ ] `AT+HTTPHEAD`
- [ ] `AT+HTTPREAD`
- [ ] `AT+HTTPDATA`
- [ ] `AT+HTTPPOSTFILE`
- [ ] `AT+HTTPREADFILE`

## FTP(S) (19)
- [ ] `AT+CFTPSSTART`
- [ ] `AT+CFTPSSTOP`
- [ ] `AT+CFTPSLOGIN`
- [ ] `AT+CFTPSLOGOUT`
- [ ] `AT+CFTPSLIST`
- [ ] `AT+CFTPSMKD`
- [ ] `AT+CFTPSRMD`
- [ ] `AT+CFTPSCWD`
- [ ] `AT+CFTPSPWD`
- [ ] `AT+CFTPSDELE`
- [ ] `AT+CFTPSGETFILE`
- [ ] `AT+CFTPSPUTFILE`
- [ ] `AT+CFTPSGET`
- [ ] `AT+CFTPSPUT`
- [ ] `AT+CFTPSSINGLEIP`
- [ ] `AT+CFTPSSIZE`
- [ ] `AT+CFTPSTYPE`
- [ ] `AT+CFTPSSLCFG`
- [ ] `AT+CFTPSMODE`

## MQTT(S) (17)
- [ ] `AT+CMQTTSTART`
- [ ] `AT+CMQTTSTOP`
- [ ] `AT+CMQTTACCQ`
- [ ] `AT+CMQTTREL`
- [ ] `AT+CMQTTSSLCFG`
- [ ] `AT+CMQTTWILLTOPIC`
- [ ] `AT+CMQTTWILLMSG`
- [ ] `AT+CMQTTCONNECT`
- [ ] `AT+CMQTTDISC`
- [ ] `AT+CMQTTTOPIC`
- [ ] `AT+CMQTTPAYLOAD`
- [ ] `AT+CMQTTPUB`
- [ ] `AT+CMQTTSUBTOPIC`
- [ ] `AT+CMQTTSUB`
- [ ] `AT+CMQTTUNSUBTOPIC`
- [ ] `AT+CMQTTUNSUB`
- [ ] `AT+CMQTTCFG`

## SSL (16)
- [ ] `AT+CSSLCFG`
- [ ] `AT+CCERTDOWN`
- [ ] `AT+CCERTLIST`
- [ ] `AT+CCERTDELE`
- [ ] `AT+CCHSET`
- [ ] `AT+CCHMODE`
- [ ] `AT+CCHSTART`
- [ ] `AT+CCHSTOP`
- [ ] `AT+CCHADDR`
- [ ] `AT+CCHSSLCFG`
- [ ] `AT+CCHCFG`
- [ ] `AT+CCHOPEN`
- [ ] `AT+CCHCLOSE`
- [ ] `AT+CCHSEND`
- [ ] `AT+CCHRECV`
- [ ] `AT+CCERTMOVE`

## TTS (3)
- [ ] `AT+CTTS`
- [ ] `AT+CTTSPARAM`
- [ ] `AT+CDTAM`

## Audio (9)
- [ ] `AT+CCMXPLAY`
- [ ] `AT+CCMXSTOP`
- [ ] `AT+CREC`
- [ ] `AT+CRTSWITCH`
- [ ] `AT+CRINGSET`
- [ ] `AT+CCODECSWITCH`
- [ ] `AT+CLDTMF`
- [ ] `AT+SIMTONE`
- [ ] `AT+STTONE`

## FOTA (2)
- [ ] `AT+CFOTA`
- [ ] `AT+LFOTA`

## SCFOTA (2)
- [ ] `AT+CAPFOTA`
- [ ] `AT+CSCFOTA`

## GNSS (16)
- [ ] `AT+CGNSSPWR`
- [ ] `AT+CGNSSTST`
- [ ] `AT+CGPSCOLD`
- [ ] `AT+CGPSWARM`
- [ ] `AT+CGPSHOT`
- [ ] `AT+CGNSSIPR`
- [ ] `AT+CGNSSMODE`
- [ ] `AT+CGNSSNMEA`
- [ ] `AT+CGPSNMEARATE`
- [ ] `AT+CGPSFTM`
- [ ] `AT+CGPSINFO`
- [ ] `AT+CGNSSINFO`
- [ ] `AT+CGNSSCMD`
- [ ] `AT+CGNSSPORTSWITCH`
- [ ] `AT+CAGPS`
- [ ] `AT+CGNSSPROD`

## WIFI (10)
- [ ] `AT+CWSTASCAN`
- [ ] `AT+CWSTASCANEX`
- [ ] `AT+CWSTASCANSYN`
- [ ] `AT+CWMAP`
- [ ] `AT+CWSSID`
- [ ] `AT+CWAUTH`
- [ ] `AT+CWMOCH`
- [ ] `AT+CWISO`
- [ ] `AT+CWMACADDR`
- [ ] `AT+CWCLICNT`

## Bluetooth (49)
- [ ] `AT+BLEPOWER`
- [ ] `AT+BLESTATUS`
- [ ] `AT+BLEHOST`
- [ ] `AT+BLEADDR`
- [ ] `AT+BLESREG`
- [ ] `AT+BLESDREG`
- [ ] `AT+BLESSAD`
- [ ] `AT+BLESSRM`
- [ ] `AT+BLESSCAD`
- [ ] `AT+BLESSCRM`
- [ ] `AT+BLESSDAD`
- [ ] `AT+BLESSDRM`
- [ ] `AT+BLESSSTART`
- [ ] `AT+BLESSSTOP`
- [ ] `AT+BLESSETADVDATA`
- [ ] `AT+BLESCLRADVDATA`
- [ ] `AT+BLESSETADVPARAM`
- [ ] `AT+BLESLSTART`
- [ ] `AT+BLESLSTOP`
- [ ] `AT+BLEADV`
- [ ] `AT+BLEDISCONN`
- [ ] `AT+BLESIND`
- [ ] `AT+BLESNTY`
- [ ] `AT+BLESRSP`
- [ ] `AT+BLECREG`
- [ ] `AT+BLECDREG`
- [ ] `AT+BLESCAN`
- [ ] `AT+BLECGDT`
- [ ] `AT+BLECCON`
- [ ] `AT+BLECDISC`
- [ ] `AT+BLECSS`
- [ ] `AT+BLECGC`
- [ ] `AT+BLECGD`
- [ ] `AT+BLECRC`
- [ ] `AT+BLECWC`
- [ ] `AT+BLECRD`
- [ ] `AT+BLECWD`
- [ ] `AT+BTPOWER`
- [ ] `AT+BTHOST`
- [ ] `AT+BTADDR`
- [ ] `AT+BTSCAN`
- [ ] `AT+BTIOCAP`
- [ ] `AT+BTPAIR`
- [ ] `AT+BTUNPAIR`
- [ ] `AT+BTPAIRED`
- [ ] `AT+BTSPPSRV`
- [ ] `AT+BTSPPPROF`
- [ ] `AT+BTSPPCONN`
- [ ] `AT+BTSPPSEND`

## CTBURST (1)
- [ ] `AT+CTBURST`

## WEBSOCKET (5)
- [ ] `AT+WSSTART`
- [ ] `AT+WSSTOP`
- [ ] `AT+WSCONNECT`
- [ ] `AT+WSDISC`
- [ ] `AT+WSSEND`

## LWM2M (10)
- [ ] `AT+LWSTART`
- [ ] `AT+LWSTOP`
- [ ] `AT+LWCNF`
- [ ] `AT+LWOPEN`
- [ ] `AT+LWCLOSE`
- [ ] `AT+LWADDOBJ`
- [ ] `AT+LWDELOBJ`
- [ ] `AT+LWREADRSP`
- [ ] `AT+LWWRITERSP`
- [ ] `AT+LWEXECUTERSP`

## COAP (8)
- [ ] `AT+COAPSTART`
- [ ] `AT+COAPSTOP`
- [ ] `AT+COAPOPEN`
- [ ] `AT+COAPCLOSE`
- [ ] `AT+COAPHEAD`
- [ ] `AT+COAPOPTION`
- [ ] `AT+COAPSEND`
- [ ] `AT+COAPSENDTX`

## SMTPS (12)
- [ ] `AT+CSMTPSCFG`
- [ ] `AT+CSMTPSSRV`
- [ ] `AT+CSMTPSAUTH`
- [ ] `AT+CSMTPSFROM`
- [ ] `AT+CSMTPSRCPT`
- [ ] `AT+CSMTPSSUB`
- [ ] `AT+CSMTPSBODY`
- [ ] `AT+CSMTPSBCH`
- [ ] `AT+CSMTPSFILE`
- [ ] `AT+CSMTPSSEND`
- [ ] `AT+CSMTPSSTOP`
- [ ] `AT+CSMTPSCLEAN`

## Telecom self-registration (2)
- [ ] `AT+HWVER`
- [ ] `AT+AUTOREGCFG`

## PSM (3)
- [ ] `AT*COMCFG`
- [ ] `AT+CPSMS`
- [ ] `AT+MEDCR`

## USB (4)
- [ ] `AT+DIALMODE`
- [ ] `AT$MYCONFIG`
- [ ] `AT+USBNETIP`
- [ ] `AT+USBNETMAC`

## JammingDetect (2)
- [ ] `AT+SJDR`
- [ ] `AT+SJDCFG`
