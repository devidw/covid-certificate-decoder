from covid_certificate_decoder import CovidCertificateDecoder

with open('sample.txt') as f:
    sample = f.read()

cert = CovidCertificateDecoder.decode(sample)
print(cert)
