from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

host_db = {}

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet:
        return

    src_mac = packet.src
    dst_mac = packet.dst
    dpid = event.dpid
    in_port = event.port

    # Store host info
    if src_mac not in host_db:
        host_db[src_mac] = (dpid, in_port)
        log.info("New Host Detected: MAC=%s Switch=%s Port=%s",
                 src_mac, dpid, in_port)
    else:
        log.info("Known Host: MAC=%s Switch=%s Port=%s",
                 src_mac, dpid, in_port)

    fm = of.ofp_flow_mod()
    fm.match.in_port = in_port
    fm.match.dl_dst = dst_mac
    fm.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))

    event.connection.send(fm)

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    msg.in_port = in_port

    event.connection.send(msg)

def launch():
    log.info("Host Discovery Controller Started")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
