from bs4 import BeautifulSoup

# Your HTML data as a string
html_data = """

            <thead>
            <tr><th hidden="">বছর</th>
            <th>
                
                
                        Short Title
                
            </th>
            <th>
                
                
                    Act No
                
            </th>
            </tr></thead>
            <tbody>
            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-1315.html">
                                    1799
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-1315.html">
                                        THE [***] WILLS AND INTESTACY REGULATION, 1799
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-1315.html">
                                    V
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-1316.html">
                                    1810
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-1316.html">
                                        THE  [***] CHARITABLE ENDOWMENTS PUBLIC BUILDINGS AND ESCHEATS REGULATION, 1810
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-1316.html">
                                    XIX
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-1317.html">
                                    1818
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-1317.html">
                                        THE [***] STATE PRISONERS REGULATION, 1818
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-1317.html">
                                    III
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-1318.html">
                                    1822
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-1318.html">
                                        THE [***] GOVERNMENT INDEMNITY REGULATION, 1822
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-1318.html">
                                    XI
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-1319.html">
                                    1825
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-1319.html">
                                        THE [***] ALLUVION AND DILUVION REGULATION, 1825
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-1319.html">
                                    XI
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-1320.html">
                                    1829
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-1320.html">
                                        THE [***] REVENUE COMMISSIONERS REGULATION, 1829
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-1320.html">
                                    I
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-1321.html">
                                    1829
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-1321.html">
                                        THE [***] SATI REGULATION, 1829
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-1321.html">
                                    XVII
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-1322.html">
                                    1833
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-1322.html">
                                        THE [***] LAND-REVENUE (SETTLEMENT AND DEPUTY COLLECTORS) REGULATION, 1833
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-1322.html">
                                    IX
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-1.html">
                                    1836
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-1.html">
                                        The Districts Act, 1836
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-1.html">
                                    XXI
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-2.html">
                                    1850
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-2.html">
                                        The Public Accountant's Default Act, 1850
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-2.html">
                                    XII
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-3.html">
                                    1850
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-3.html">
                                        The Judicial Officer's Protection Act, 1850 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-3.html">
                                    XVIII
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-4.html">
                                    1850
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-4.html">
                                        The Public Servants (Inquiries) Act, 1850 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-4.html">
                                    XXXVII
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-5.html">
                                    1851
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-5.html">
                                        The Tolls Act, 1851 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-5.html">
                                    VIII
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-6.html">
                                    1855
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-6.html">
                                        The Legal Representative Suits Act, 1855
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-6.html">
                                    XII
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-7.html">
                                    1855
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-7.html">
                                        The Fatal Accidents Act, 1855
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-7.html">
                                    XIII
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-8.html">
                                    1856
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-8.html">
                                        The Bills of Lading Act, 1856 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-8.html">
                                    IX
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-9.html">
                                    1856
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-9.html">
                                        The Hindu Widow's Re-marriage Act, 1856 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-9.html">
                                    XV
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-10.html">
                                    1860
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-10.html">
                                        The Societies Registration Act, 1860 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-10.html">
                                    XXI
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-11.html">
                                    1860
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-11.html">
                                        The Penal Code, 1860 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-11.html">
                                    XLV
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-12.html">
                                    1861
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-12.html">
                                        The Police Act, 1861 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-12.html">
                                    V
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-13.html">
                                    1861
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-13.html">
                                        The Stage-Carriages Act, 1861 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-13.html">
                                    XVI
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-14.html">
                                    1864
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-14.html">
                                        The Canals Act, 1864 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-14.html">
                                    V
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-15.html">
                                    1865
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-15.html">
                                        The Carriers Act, 1865 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-15.html">
                                    III
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-16.html">
                                    1867
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-16.html">
                                        The Public Gambling Act, 1867 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-16.html">
                                    II
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-17.html">
                                    1867
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-17.html">
                                        The Acting Judges Act, 1867 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-17.html">
                                    XVI
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-18.html">
                                    1867
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-18.html">
                                        The Sarais Act, 1867 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-18.html">
                                    XXII
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-19.html">
                                    1868
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-19.html">
                                        The Alluvion (Amendment) Act, 1868 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-19.html">
                                    IV
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-20.html">
                                    1869
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-20.html">
                                        The Divorce Act, 1869 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-20.html">
                                    IV
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-21.html">
                                    1870
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-21.html">
                                        The Court-fees Act, 1870 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-21.html">
                                    VII
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-22.html">
                                    1871
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-22.html">
                                        The Cattle-trespass Act, 1871 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-22.html">
                                    I
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-23.html">
                                    1871
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-23.html">
                                        The Pensions Act, 1871  
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-23.html">
                                    XXIII
                            </a>
                        </td>
                    </tr>
                

            
                
                    <tr>
                        <td hidden="">
                            <a href="/act-24.html">
                                    1872
                            </a>
                        </td>
                        <td>
                            
                            
                            
                                <a href="/act-24.html">
                                        The Evidence Act, 1872 
                                </a>
                            
                        </td>
                        <td>
                            <a href="/act-24.html">
                                    I
                            </a>
                        </td>
                    </tr>
                

            
            </tbody>
        
"""

# Parse the HTML data
soup = BeautifulSoup(html_data, 'html.parser')

# Base URL to replace the links
root_url = "root_url/laws/volume-1"

# Generate the markdown table with updated column headers
markdown_table = "| বছর | সংক্ষিপ্ত শিরোনাম | আইন নং |\n| --- | --- | --- |\n"

for row in soup.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all('td')
    
    # Extract the relevant data from the cells
    year = cells[0].get_text(strip=True)
    short_title = cells[1].get_text(strip=True)
    act_no = cells[2].get_text(strip=True)
    
    # Extract the act number for the new URL format
    act_link = cells[1].find('a')['href']
    act_id = act_link.split('-')[1].split('.')[0]  # Extract act ID from link
    
    # Format the new URL
    new_url = f"{root_url}/act-details-{act_id}/"
    
    # Append row to the markdown table with modified links
    markdown_table += f"| {year} | [{short_title}]({new_url}) | {act_no} |\n"

# Save the markdown table to a file
with open("table.md", "w", encoding="utf-8") as file:
    file.write(markdown_table)

print("Markdown table has been saved to 'table.md'.")