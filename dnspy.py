import dns
import dns.resolver
import dns.query
import dns.reversename
import dns.name
import dns.zone

dominio =  ""
dominio1 = ""
address = ""

respuestaA = dns.resolver.query(dominio, 'A')
respuestaAAAA = dns.resolver.query(dominio, 'AAAA')
respuestaSOA = dns.resolver.query(dominio, 'SOA')
respuestaTXT = dns.resolver.query(dominio, 'TXT')
respuestaMX = dns.resolver.query(dominio, 'MX')
respuestaNS = dns.resolver.query(dominio, 'NS')

n = dns.name.from_text(dominio)
n1 = dns.name.from_text(dominio1)

print n1.is_subdomain(n)
print n1.labels
print n1.relativize


n = dns.reversename.from_address(address)
n1 = dns.reversename.to_address(n)

n = dns.query.xfr('173.194.34.200', 'thehackerway.com')
z = dns.zone.from_xfr(n)
