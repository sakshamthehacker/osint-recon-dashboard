import streamlit as st
import json
from modules.whois_lookup import get_whois_info
from modules.dns_lookup import get_dns_records
from modules.ip_lookup import resolve_ip, geolocate_ip
from modules.subdomain_lookup import get_subdomains
from modules.breach_check import check_breach
from modules.username_check import check_username
from modules.ai_summary import summarize_findings
from modules.db import init_db, save_scan, get_all_scans

st.set_page_config(page_title="OSINT Recon Dashboard", page_icon="🔍", layout="wide")

init_db()

page = st.sidebar.radio("Navigate", ["Scanner", "Scan History"])

st.title("OSINT Recon Dashboard")

if page == "Scanner":
    col1, col2, col3 = st.columns(3)
    with col1:
        domain = st.text_input("Domain (e.g. google.com)").strip()
    with col2:
        email = st.text_input("Email (optional, for breach check)").strip()
    with col3:
        username = st.text_input("Username (optional, for platform search)").strip()

    if st.button("Scan"):
        if domain:
            with st.spinner("Running OSINT scan... this may take a few seconds"):
                whois_data = get_whois_info(domain)
                dns_data = get_dns_records(domain)
                ip = resolve_ip(domain)
                ip_geo = {"error": "Could not resolve IP for this domain"} if ip.startswith("Error") else geolocate_ip(ip)
                subs = get_subdomains(domain)
                breach_result = check_breach(email) if email else None
                username_result = check_username(username) if username else None

                tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
                    ["WHOIS", "DNS", "IP / Geo", "Subdomains", "Breach Check", "Username Search", "AI Risk Assessment"]
                )

                with tab1:
                    st.json(whois_data)

                with tab2:
                    st.json(dns_data)

                with tab3:
                    st.write(f"IP: {ip}")
                    st.json(ip_geo)

                with tab4:
                    st.write(f"Found {len(subs)} subdomains")
                    st.table(subs)

                with tab5:
                    if breach_result:
                        st.json(breach_result)
                    else:
                        st.info("Enter an email above to check for breaches.")

                with tab6:
                    if username_result:
                        for platform, info in username_result.items():
                            st.write(f"**{platform}**: {info}")
                    else:
                        st.info("Enter a username above to search across platforms.")

                with tab7:
                    all_data = {
                        "domain": domain,
                        "whois": whois_data,
                        "dns": dns_data,
                        "ip_geo": ip_geo,
                        "subdomains": subs,
                    }
                    if breach_result:
                        all_data["breach_check"] = breach_result
                    if username_result:
                        all_data["username_check"] = username_result

                    summary = summarize_findings(all_data)
                    st.markdown(summary)

                    all_data["ai_summary"] = summary
                    save_scan(domain, all_data)
        else:
            st.warning("Please enter a domain.")

elif page == "Scan History":
    st.subheader("Past Scans")
    scans = get_all_scans()

    if scans:
        for scan_id, target, timestamp, results in scans:
            with st.expander(f"{target} — {timestamp}"):
                data = json.loads(results)
                if "ai_summary" in data:
                    st.markdown(data["ai_summary"])
                    st.divider()
                st.json(data)
    else:
        st.info("No scans yet. Run a scan from the Scanner page first.")