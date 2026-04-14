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

	log.info("New Host Detected: MAC=%s Switch=%s Port=%s", src_mac, dpid, in_port)
	
	msg = of.ofp_packet_out()
	msg.data = event.ofp
	msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
	msg.in_port = in_port
	event.connection.send(msg)

def launch():
	log.info("Host Discovery Controller Starter")
	core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

