#!/usr/bin/env python3
"""
Append all missing Article 30 content to the markdown file
"""

# Read the extracted content
with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/article30_extracted_raw.txt', 
          'r', encoding='utf-8') as f:
    raw_content = f.read()

# Read existing markdown
with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/Article_30_Development_ReProcedures.md', 
          'r', encoding='utf-8') as f:
    existing_content = f.read()

# I'll manually format the content based on what I saw in the raw file
# Starting with section 1 (Exemptions) through the end

new_content = """

**1. Exemptions**

The following shall be exempt from the procedures of this Article:

a. A transaction between owners of adjoining unplatted property that involves only a change in the boundary between the land owned by such persons provided no additional tracts are created and such tracts comply with the lot size and setback standarthe underlying zoning district.

b. Property, which is created by adjoining unplatted tracts parcels that involve the combination of contiguous, parcels of land into one larger parcel.

c. The conveyance of land for street or railroad right-of-way, utility or drainage easements, or other public utility purposes subject to local, state, or federal regulations, and where no new street or access easements are created.

d. The conveyance of land for public recreation, trails or similar easements and public purposes.

e. The division of land into parcels 40 acresrger in area.

f. The division of land into parcels 40 acres or larger in area after the date of adoption of this Article, provided such tracts have at least 100 total feet of frontage along a state or county maintained roadway, and access to the tracts and any remnant parcels comply with the county or state minimum sight distance requirements.

g. The division of land into cemetery plots.

h. The division of land by any court action pursuant to the law of eminent domain.

i. A division of property through the probate of an estate, or by order or judgmenurt of law of competent jurisdiction of the State of Missouri.

## 30.5 Minor Subdivision

A Minor Subdivision refers to a reconfiguration of land that contains 4 or fewer residential lots of not less than 5.0 acres. The intent is to streamline the process to accommodate subdivisions of land that are determined to be minor in nature. It requires possible Rezoning, technical reviews, and Final Plat review and approvals by the Planning and Zoning Commission and the County Commission. After considering all prior subdivision activity on the greater parcel, a determination will be he Planning and Zoning Administrator whether or not the application may proceed as a Minor Subdivision.

### A. Prerequisites

1. Creates no more than 4 residential lots of not less than 5.0 acres
2. Does not require the extension of public facilities or the creating of significant public improvements, as determined by the Planning and Zoning Administrator
3. Has access to an existing street and does not involve any new interior streets
4. Shall be under one ownership
5. Shall be split from one contiguous parcel
 create a nonconforming lot
7. Does not contain a "phased development" plan
8. In the case of an existing nonconforming parcel, does not increase the nonconformity
9. Not more than one Minor Subdivision involving any part of the original property per every 5 years
10. Does not adversely affect the remainder of the parcel or adjoining properties and is not in conflict with any provisions of the Ray County Comprehensive Plan or these regulations.

### B. Process

**1. Pre-application Meet**

Applicants may schedule and attend a pre-application meeting with Planning and Zoning Department staff prior to submitting an application for review under this Article.

**2. Application Filing**

A Minor Subdivision application shall be completed and submitted to the Planning and Zoning Department on forms available in the Planning and Zoning Department. All required information must be filed with the Planning and Zoning Department at least 15 days prior to a regular meeting of the Planning and Zoning Commission at which the Finalis to be considered.

**3. Final Plat**

A Final Plat prepared by a registered surveyor shall be submitted 15 days prior to regular meeting of Planning and Zoning Commission and shall conform to the requirements of Figure 30.6-2.

**4. Rezoning and/or Final Plat Application**

A completed application for Final Plat, along with the appropriate application fees, shall be submitted at least 15 days prior to the meeting at which the Planning and Zoning Commission shall review the application. If Rezoning, application and appropriate application fees shall be submitted at let 15 working days before Planning and Zoning meeting.

**5. Planning and Zoning Department's Review and Report**

The Planning and Zoning Department shall review each proposed Final Plat application and provide a report to the Planning and Zoning Commission.

**6. Planning and Zoning Commission Review and Decision**

Within 30 days of receipt of a complete Final Plat application, the Planning and Zoning Commission shall review the Final Plat and take action on the application based on the Approval Criteria of [Article 30.3F](#f-approval-criteria).

a. **Approval Criteria**

Theg and Zoning Commission may approve final Plat if they determine that all of following approval criteria has been met:

   (1) The subdivision complies with zoning regulations of the district in which it is located, the Subdivision Design and Improvement Standards of [Article 80](Article_80_Subdivision_Design_Improvements.md) and with all other applicable standards of these Zoning Regulations; and

   (2) Adequate public safety, transportation and utility facilities/services will be available to serve the subdivision whileaintaining adequate levels of service for existing development.

b. **Transmittal**

Transmittal of the recommendation to the County Commission shall be made within 30 days of the Planning and Zoning Commission's hearing.

c. **Denials**

A recommendation of denial of a Final Plat by the Planning and Zoning Commission shall be forwarded to the County Commission for action, unless the applicant requests the application be withdrawn in writing within 30 days of the public hearing.

d. **Appeal*n
Any person aggrieved by a decision of the Planning and Zoning Commission on an application may appeal to the Ray County Commission.

**7. County Commission Review and Decision**

After receiving the recommendation of the Planning and Zoning Commission, the County Commission shall take action on the application based on the Approval Criteria of [Article 30.3F](#f-approval-criteria).

a. **Approval Criteria**

A Final Plat may be approved by the County Commission if they determine that the application complies with the Zoning Regulations.

**8.  Final Plat Approval**

The County Commission's approval of the Final Plat shall lapse and be of no further effect if the Final Plat is not recorded with the Recorder of Deeds within 1 year of the County Commission's approval.

**9. Appeals**

Any person aggrieved by a decision of the County Commission on a Final Plat Application may present to the Circuit Court of Ray County a petition, duly verified, setting forth that such decision is illegal, in whole or in part, specifying the grounds of the illegality. Such petition shall be presented to the Court withinf the date of the County Commission's decision on the matter.

**10. Pre-application Conference**

Applicants for subdivisions are encouraged to discuss possible development site design possibilities and related issues with the Planning and Zoning Department prior to submission of any plat.
"""

# Write the combined content
with open('C:/Users/KurtBognar/Downloads/RayCountyZoning/Article_30_Development_Review_Procedures.md', 
          'w', encoding='utf-8') as f:
    f.write(existing_content + new_content)

print("Successfully ed 30.5 Minor Subdivision section!")
print(f"New file size: {len(existing_content + new_content)} characters")
