# ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) - Requirements Extraction

- **Standard:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN)
- **Version:** 2011/2016/2021/2024
- **Source:** https://cdn.standards.iteh.ai/samples/54499/2a977e03a16341ef904152ef97a0d74b/ISO-15765-2-2011.pdf
- **Extraction date:** 2026-09-09
- **Extraction method:** PDF text extraction + web content parsing

## Extraction Statistics

- **Clauses detected:** 45
- **Requirements extracted:** 51
- **Source text length:** 20156 characters

> In accordance with US-NORM-003 / RM-NORM-003, each requirement is marked according to its verification status.
> Requirements whose source passage was found in the extracted text are marked Verified.
> Requirements inferred from the document structure but not directly verified are marked Candidate.

## Table of Contents

- [iso-15765-9 - Transport](#iso-15765-9)
- [iso-15765-10 - Transport](#iso-15765-10)
- [iso-15765-3 - Terms and definitions](#iso-15765-3)
- [iso-15765-1 - Scope](#iso-15765-1)
- [iso-15765-5 - Overview of ISO](#iso-15765-5)
- [iso-15765-6 - Application](#iso-15765-6)
- [iso-15765-7 - Application](#iso-15765-7)
- [iso-15765-12 - Physical](#iso-15765-12)
- [iso-15765-8 - Transport](#iso-15765-8)
- [iso-15765-11 - Communication](#iso-15765-11)
- [iso-15765-3.2 - Abbreviated terms](#iso-15765-3-2)
- [iso-15765-4.2 - Abbreviated terms](#iso-15765-4-2)
- [iso-15765-5.1 - General](#iso-15765-5-1)
- [iso-15765-6.2 - Mapping of transport and network layer attributes to CAN data frames](#iso-15765-6-2)
- [iso-15765-6.3 - Diagnostic gateway](#iso-15765-6-3)
- [iso-15765-6.3.2 - Bit rate](#iso-15765-6-3-2)
- [iso-15765-6.5 - Support of ECUNAME reporting](#iso-15765-6-5)
- [iso-15765-7.1 - Overview](#iso-15765-7-1)
- [iso-15765-7.2 - DoCAN use case clusters](#iso-15765-7-2)
- [iso-15765-7.3 - Data type definitions](#iso-15765-7-3)
- [iso-15765-8.1 - Use case](#iso-15765-8-1)
- [iso-15765-8.2 - Use case](#iso-15765-8-2)
- [iso-15765-8.2.1 - Data](#iso-15765-8-2-1)
- [iso-15765-8.2.2 - Data](#iso-15765-8-2-2)
- [iso-15765-8.2.3 - Data](#iso-15765-8-2-3)
- [iso-15765-8.2.4 - Data](#iso-15765-8-2-4)
- [iso-15765-8.2.5 - Change](#iso-15765-8-2-5)
- [iso-15765-8.2.6 - Change](#iso-15765-8-2-6)
- [iso-15765-8.3 - Use case](#iso-15765-8-3)
- [iso-15765-8.3.5 - Parameter](#iso-15765-8-3-5)
- [iso-15765-8.3.6 - Parameter](#iso-15765-8-3-6)
- [iso-15765-9.1 - General](#iso-15765-9-1)
- [iso-15765-9.5 - Flow](#iso-15765-9-5)
- [iso-15765-10.1 - General](#iso-15765-10-1)
- [iso-15765-10.2 - Parameter](#iso-15765-10-2)
- [iso-15765-10.2.1 - Timing](#iso-15765-10-2-1)
- [iso-15765-10.2.2 - Definition](#iso-15765-10-2-2)
- [iso-15765-10.3 - Addressing](#iso-15765-10-3)
- [iso-15765-10.3.3 - Physical](#iso-15765-10-3-3)
- [iso-15765-10.5 - Mapping](#iso-15765-10-5)
- [iso-15765-10.6 - Flow](#iso-15765-10-6)
- [iso-15765-10.7 - Addressing](#iso-15765-10-7)
- [iso-15765-11.1 - General](#iso-15765-11-1)
- [iso-15765-12.1 - General](#iso-15765-12-1)
- [iso-15765-12.2 - Bit rate](#iso-15765-12-2)
- [iso-15765-REQ20 - CAN ID plus the first byte of the CAN payload; both the CAN ID and the byte insi...](#iso-15765-REQ20)
- [iso-15765-REQ21 - Once this information has been received, the sender starts to send frames contai...](#iso-15765-REQ21)
- [iso-15765-REQ22 - Creation and basic usage of an ISO-TP socket -----------------------------------...](#iso-15765-REQ22)
- [iso-15765-REQ23 - C s = socket(PF_CAN, SOCK_DGRAM, CAN_ISOTP); After the socket has been successfu...](#iso-15765-REQ23)
- [iso-15765-REQ24 - RX CAN ID shall also be specified, unless broadcast flags have been set through ...](#iso-15765-REQ24)
- [iso-15765-REQ25 - To set the transmission time to ``0``, the ``CAN_ISOTP_FRAME_TXTIME_ZERO`` macro...](#iso-15765-REQ25)

---

## iso-15765-9 - Transport

- **Official ID:** iso-15765-9
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 9
- **Source reference:** 2011/2016/2021/2024, clause 9
- **Status:** Candidate

- **Description:** Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced

---

## iso-15765-10 - Transport

- **Official ID:** iso-15765-10
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 10
- **Source reference:** 2011/2016/2021/2024, clause 10
- **Status:** Candidate

- **Description:** Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced

---

## iso-15765-3 - Terms and definitions

- **Official ID:** iso-15765-3
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 3
- **Source reference:** 2011/2016/2021/2024, clause 3
- **Status:** Candidate

- **Description:** Terms and definitions 3.2 Abbreviated terms 4 Conventions 5 Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control

---

## iso-15765-1 - Scope

- **Official ID:** iso-15765-1
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 1
- **Source reference:** 2011/2016/2021/2024, clause 1
- **Status:** Candidate

- **Description:** Scope 2 Normative references 3 Terms, definitions and abbreviated terms 3.1 Terms and definitions 3.2 Abbreviated terms 4 Conventions 5 Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 A

---

## iso-15765-5 - Overview of ISO

- **Official ID:** iso-15765-5
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 5
- **Source reference:** 2011/2016/2021/2024, clause 5
- **Status:** Candidate

- **Description:** Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame

---

## iso-15765-6 - Application

- **Official ID:** iso-15765-6
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 6
- **Source reference:** 2011/2016/2021/2024, clause 6
- **Status:** Verified

- **Description:** Application 6.1 Vehicle communication initialisation sequence 6.1.1 OBDonUDS protocol identification 6.1.2 OBDonEDS protocol identification 6.1.3 Others 6.2 External test equipment communication initialisation sequence 6.3 Bit rate validation procedure 6.3.1 bitrateRecord 6.3.2 Bit rate validation 6.3.3 External test equipment error detection provisions 6.4 CAN identifier validation procedure 6.4.1 CAN identifier validation procedure OBDonEDS 6.4.2 CAN identifier validation procedure OBDonUDS 6.5 Support of ECUNAME reporting 7 Application layer (AL) 8 Session layer (SL) 9 Transport layer (TL) 10 Network layer (NL) 10.1 General 10.2 Parameter definitions 10.2.1 Timing parameter values 10.2.2 Definition of flow control parameter values 10.2.3 Maximum number of OBDonUDS or OBDonEDS ECUs 10.3 Addressing formats 10.3.1 Normal and normal fixed addressing format 10.3.2 Functional addressing 10.3.3 Physical addressing 10.4 CAN identifier requirements 10.4.1 External test equipment 10.4.2 OBDonUDS or OBDonEDS server/ECU 10.5 Mapping of diagnostic addresses 10.5.1 OBDonUDS/OBDonEDS CAN identifiers 10.5.2 11-bit CAN identifiers 10.5.3 29-bit CAN identifiers 11 Data link layer (DLL) 12 Physical layer (PHY) 12.1 General 12.2 Bit rates ISO 15765-4:2021 specifies the requirements for emissions-related systems. The vehicle communication initialisation sequence shall be performed according to the specified protocol identification procedure. The external test equipment communication initialisation sequence shall be performed before any diagnostic communication. The bit rate validation procedure shall be executed to ensure correct communication. The CAN identifier validation procedure shall be performed for both OBDonEDS and OBDonUDS protocols. The application layer shall provide the diagnostic services. The session layer shall manage the diagnostic session. The transport layer shall provide the transport protocol services. The network layer shall provide the network layer services w

---

## iso-15765-7 - Application

- **Official ID:** iso-15765-7
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 7
- **Source reference:** 2011/2016/2021/2024, clause 7
- **Status:** Verified

- **Description:** Application 6.1 Vehicle communication initialisation sequence 6.1.1 OBDonUDS protocol identification 6.1.2 OBDonEDS protocol identification 6.1.3 Others 6.2 External test equipment communication initialisation sequence 6.3 Bit rate validation procedure 6.3.1 bitrateRecord 6.3.2 Bit rate validation 6.3.3 External test equipment error detection provisions 6.4 CAN identifier validation procedure 6.4.1 CAN identifier validation procedure OBDonEDS 6.4.2 CAN identifier validation procedure OBDonUDS 6.5 Support of ECUNAME reporting 7 Application layer (AL) 8 Session layer (SL) 9 Transport layer (TL) 10 Network layer (NL) 10.1 General 10.2 Parameter definitions 10.2.1 Timing parameter values 10.2.2 Definition of flow control parameter values 10.2.3 Maximum number of OBDonUDS or OBDonEDS ECUs 10.3 Addressing formats 10.3.1 Normal and normal fixed addressing format 10.3.2 Functional addressing 10.3.3 Physical addressing 10.4 CAN identifier requirements 10.4.1 External test equipment 10.4.2 OBDonUDS or OBDonEDS server/ECU 10.5 Mapping of diagnostic addresses 10.5.1 OBDonUDS/OBDonEDS CAN identifiers 10.5.2 11-bit CAN identifiers 10.5.3 29-bit CAN identifiers 11 Data link layer (DLL) 12 Physical layer (PHY) 12.1 General 12.2 Bit rates ISO 15765-4:2021 specifies the requirements for emissions-related systems. The vehicle communication initialisation sequence shall be performed according to the specified protocol identification procedure. The external test equipment communication initialisation sequence shall be performed before any diagnostic communication. The bit rate validation procedure shall be executed to ensure correct communication. The CAN identifier validation procedure shall be performed for both OBDonEDS and OBDonUDS protocols. The application layer shall provide the diagnostic services. The session layer shall manage the diagnostic session. The transport layer shall provide the transport protocol services. The network layer shall provide the network layer services w

---

## iso-15765-12 - Physical

- **Official ID:** iso-15765-12
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 12
- **Source reference:** 2011/2016/2021/2024, clause 12
- **Status:** Verified

- **Description:** Physical addressing 10.4 CAN identifier requirements 10.4.1 External test equipment 10.4.2 OBDonUDS or OBDonEDS server/ECU 10.5 Mapping of diagnostic addresses 10.5.1 OBDonUDS/OBDonEDS CAN identifiers 10.5.2 11-bit CAN identifiers 10.5.3 29-bit CAN identifiers 11 Data link layer (DLL) 12 Physical layer (PHY) 12.1 General 12.2 Bit rates ISO 15765-4:2021 specifies the requirements for emissions-related systems. The vehicle communication initialisation sequence shall be performed according to the specified protocol identification procedure. The external test equipment communication initialisation sequence shall be performed before any diagnostic communication. The bit rate validation procedure shall be executed to ensure correct communication. The CAN identifier validation procedure shall be performed for both OBDonEDS and OBDonUDS protocols. The application layer shall provide the diagnostic services. The session layer shall manage the diagnostic session. The transport layer shall provide the transport protocol services. The network layer shall provide the network layer services with the specified timing parameters. The data link layer shall comply with ISO 11898-1. The physical layer shall support the specified bit rates. ===LOCAL_SOURCE=== .. SPDX-License-Identifier: (GPL-2.0 OR BSD-3-Clause) ==================== ISO 15765-2 (ISO-TP) ==================== Overview ======== ISO 15765-2, also known as ISO-TP, is a transport protocol specifically defined for diagnostic communication on CAN. It is widely used in the automotive industry, for example as the transport protocol for UDSonCAN (ISO 14229-3) or emission-related diagnostic services (ISO 15031-5). ISO-TP can be used both on CAN CC (aka Classical CAN) and CAN FD (CAN with Flexible Datarate) based networks. It is also designed to be compatible with a CAN network using SAE J1939 as data link layer (however, this is not a requirement). Specifications used ------------------- * ISO 15765-2:2024 : Road vehicles - Diag

---

## iso-15765-8 - Transport

- **Official ID:** iso-15765-8
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8
- **Source reference:** 2011/2016/2021/2024, clause 8
- **Status:** Candidate

- **Description:** Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced

---

## iso-15765-11 - Communication

- **Official ID:** iso-15765-11
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 11
- **Source reference:** 2011/2016/2021/2024, clause 11
- **Status:** Verified

- **Description:** Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network layer communication protocol for the exchange of data between network nodes, e.g. from ECU to ECU, or between external test equipment and an ECU. If the data to be transferred do not fit into a single CAN frame, a segmentation method is provided. The network layer shall provide services to higher layers. The service interface shall define a set of services. The transport protocol shall support segmentation of messages that exceed the size of a single CAN frame. The flow control shall manage the data flow between sender and receiver. The addressing shall support different addressing formats including normal, normal fixed, functional and physical addressing. The timing parameters shall be defined for all protocol operations. The CAN identifier requirements shall be met for both 11-bit and 29-bit identifiers. The data link layer shall comply with ISO 11898-1. The physical layer shall be specified according to the com

---

## iso-15765-3.2 - Abbreviated terms

- **Official ID:** iso-15765-3.2
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 3.2
- **Source reference:** 2011/2016/2021/2024, clause 3.2
- **Status:** Candidate

- **Description:** Abbreviated terms 4 Conventions 5 Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.

---

## iso-15765-4.2 - Abbreviated terms

- **Official ID:** iso-15765-4.2
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 4.2
- **Source reference:** 2011/2016/2021/2024, clause 4.2
- **Status:** Candidate

- **Description:** Abbreviated terms 4 Conventions 5 Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.

---

## iso-15765-5.1 - General

- **Official ID:** iso-15765-5.1
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 5.1
- **Source reference:** 2011/2016/2021/2024, clause 5.1
- **Status:** Candidate

- **Description:** General information and use case definition Contents: 1 Scope 2 Normative references 3 Terms, definitions and abbreviated terms 3.1 Terms and definitions 3.2 Abbreviated terms 4 Conventions 5 Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parame

---

## iso-15765-6.2 - Mapping of transport and network layer attributes to CAN data frames

- **Official ID:** iso-15765-6.2
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 6.2
- **Source reference:** 2011/2016/2021/2024, clause 6.2
- **Status:** Candidate

- **Description:** Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer se

---

## iso-15765-6.3 - Diagnostic gateway

- **Official ID:** iso-15765-6.3
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 6.3
- **Source reference:** 2011/2016/2021/2024, clause 6.3
- **Status:** Candidate

- **Description:** Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Rece

---

## iso-15765-6.3.2 - Bit rate

- **Official ID:** iso-15765-6.3.2
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 6.3.2
- **Source reference:** 2011/2016/2021/2024, clause 6.3.2
- **Status:** Verified

- **Description:** Bit rate validation procedure 6.3.1 bitrateRecord 6.3.2 Bit rate validation 6.3.3 External test equipment error detection provisions 6.4 CAN identifier validation procedure 6.4.1 CAN identifier validation procedure OBDonEDS 6.4.2 CAN identifier validation procedure OBDonUDS 6.5 Support of ECUNAME reporting 7 Application layer (AL) 8 Session layer (SL) 9 Transport layer (TL) 10 Network layer (NL) 10.1 General 10.2 Parameter definitions 10.2.1 Timing parameter values 10.2.2 Definition of flow control parameter values 10.2.3 Maximum number of OBDonUDS or OBDonEDS ECUs 10.3 Addressing formats 10.3.1 Normal and normal fixed addressing format 10.3.2 Functional addressing 10.3.3 Physical addressing 10.4 CAN identifier requirements 10.4.1 External test equipment 10.4.2 OBDonUDS or OBDonEDS server/ECU 10.5 Mapping of diagnostic addresses 10.5.1 OBDonUDS/OBDonEDS CAN identifiers 10.5.2 11-bit CAN identifiers 10.5.3 29-bit CAN identifiers 11 Data link layer (DLL) 12 Physical layer (PHY) 12.1 General 12.2 Bit rates ISO 15765-4:2021 specifies the requirements for emissions-related systems. The vehicle communication initialisation sequence shall be performed according to the specified protocol identification procedure. The external test equipment communication initialisation sequence shall be performed before any diagnostic communication. The bit rate validation procedure shall be executed to ensure correct communication. The CAN identifier validation procedure shall be performed for both OBDonEDS and OBDonUDS protocols. The application layer shall provide the diagnostic services. The session layer shall manage the diagnostic session. The transport layer shall provide the transport protocol services. The network layer shall provide the network layer services with the specified timing parameters. The data link layer shall comply with ISO 11898-1. The physical layer shall support the specified bit rates. ===LOCAL_SOURCE=== .. SPDX-License-Identifier: (GPL-2.0 OR BSD-3-Clause) ===

---

## iso-15765-6.5 - Support of ECUNAME reporting

- **Official ID:** iso-15765-6.5
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 6.5
- **Source reference:** 2011/2016/2021/2024, clause 6.5
- **Status:** Verified

- **Description:** Support of ECUNAME reporting 7 Application layer (AL) 8 Session layer (SL) 9 Transport layer (TL) 10 Network layer (NL) 10.1 General 10.2 Parameter definitions 10.2.1 Timing parameter values 10.2.2 Definition of flow control parameter values 10.2.3 Maximum number of OBDonUDS or OBDonEDS ECUs 10.3 Addressing formats 10.3.1 Normal and normal fixed addressing format 10.3.2 Functional addressing 10.3.3 Physical addressing 10.4 CAN identifier requirements 10.4.1 External test equipment 10.4.2 OBDonUDS or OBDonEDS server/ECU 10.5 Mapping of diagnostic addresses 10.5.1 OBDonUDS/OBDonEDS CAN identifiers 10.5.2 11-bit CAN identifiers 10.5.3 29-bit CAN identifiers 11 Data link layer (DLL) 12 Physical layer (PHY) 12.1 General 12.2 Bit rates ISO 15765-4:2021 specifies the requirements for emissions-related systems. The vehicle communication initialisation sequence shall be performed according to the specified protocol identification procedure. The external test equipment communication initialisation sequence shall be performed before any diagnostic communication. The bit rate validation procedure shall be executed to ensure correct communication. The CAN identifier validation procedure shall be performed for both OBDonEDS and OBDonUDS protocols. The application layer shall provide the diagnostic services. The session layer shall manage the diagnostic session. The transport layer shall provide the transport protocol services. The network layer shall provide the network layer services with the specified timing parameters. The data link layer shall comply with ISO 11898-1. The physical layer shall support the specified bit rates. ===LOCAL_SOURCE=== .. SPDX-License-Identifier: (GPL-2.0 OR BSD-3-Clause) ==================== ISO 15765-2 (ISO-TP) ==================== Overview ======== ISO 15765-2, also known as ISO-TP, is a transport protocol specifically defined for diagnostic communication on CAN. It is widely used in the automotive industry, for example as the transport protocol

---

## iso-15765-7.1 - Overview

- **Official ID:** iso-15765-7.1
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 7.1
- **Source reference:** 2011/2016/2021/2024, clause 7.1
- **Status:** Candidate

- **Description:** Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame

---

## iso-15765-7.2 - DoCAN use case clusters

- **Official ID:** iso-15765-7.2
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 7.2
- **Source reference:** 2011/2016/2021/2024, clause 7.2
- **Status:** Candidate

- **Description:** DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addr

---

## iso-15765-7.3 - Data type definitions

- **Official ID:** iso-15765-7.3
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 7.3
- **Source reference:** 2011/2016/2021/2024, clause 7.3
- **Status:** Candidate

- **Description:** Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network lay

---

## iso-15765-8.1 - Use case

- **Official ID:** iso-15765-8.1
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.1
- **Source reference:** 2011/2016/2021/2024, clause 8.1
- **Status:** Candidate

- **Description:** Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br time

---

## iso-15765-8.2 - Use case

- **Official ID:** iso-15765-8.2
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.2
- **Source reference:** 2011/2016/2021/2024, clause 8.2
- **Status:** Candidate

- **Description:** Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br time

---

## iso-15765-8.2.1 - Data

- **Official ID:** iso-15765-8.2.1
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.2.1
- **Source reference:** 2011/2016/2021/2024, clause 8.2.1
- **Status:** Candidate

- **Description:** Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independ

---

## iso-15765-8.2.2 - Data

- **Official ID:** iso-15765-8.2.2
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.2.2
- **Source reference:** 2011/2016/2021/2024, clause 8.2.2
- **Status:** Candidate

- **Description:** Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independ

---

## iso-15765-8.2.3 - Data

- **Official ID:** iso-15765-8.2.3
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.2.3
- **Source reference:** 2011/2016/2021/2024, clause 8.2.3
- **Status:** Candidate

- **Description:** Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independ

---

## iso-15765-8.2.4 - Data

- **Official ID:** iso-15765-8.2.4
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.2.4
- **Source reference:** 2011/2016/2021/2024, clause 8.2.4
- **Status:** Candidate

- **Description:** Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independ

---

## iso-15765-8.2.5 - Change

- **Official ID:** iso-15765-8.2.5
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.2.5
- **Source reference:** 2011/2016/2021/2024, clause 8.2.5
- **Status:** Candidate

- **Description:** ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network layer communication protocol for the exchange of data between network nodes, e.g. from ECU to ECU, or between external test equipment and an ECU. If the data to be transferred do not fit into a single CAN

---

## iso-15765-8.2.6 - Change

- **Official ID:** iso-15765-8.2.6
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.2.6
- **Source reference:** 2011/2016/2021/2024, clause 8.2.6
- **Status:** Candidate

- **Description:** ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network layer communication protocol for the exchange of data between network nodes, e.g. from ECU to ECU, or between external test equipment and an ECU. If the data to be transferred do not fit into a single CAN

---

## iso-15765-8.3 - Use case

- **Official ID:** iso-15765-8.3
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.3
- **Source reference:** 2011/2016/2021/2024, clause 8.3
- **Status:** Candidate

- **Description:** Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br time

---

## iso-15765-8.3.5 - Parameter

- **Official ID:** iso-15765-8.3.5
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.3.5
- **Source reference:** 2011/2016/2021/2024, clause 8.3.5
- **Status:** Candidate

- **Description:** Parameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network layer communication protocol for the exchange of data between network nodes, e.g. from ECU to ECU, or between external test equipment and an ECU. If the data to be transferred do not fit into a single CAN frame,

---

## iso-15765-8.3.6 - Parameter

- **Official ID:** iso-15765-8.3.6
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 8.3.6
- **Source reference:** 2011/2016/2021/2024, clause 8.3.6
- **Status:** Candidate

- **Description:** Parameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network layer communication protocol for the exchange of data between network nodes, e.g. from ECU to ECU, or between external test equipment and an ECU. If the data to be transferred do not fit into a single CAN frame,

---

## iso-15765-9.1 - General

- **Official ID:** iso-15765-9.1
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 9.1
- **Source reference:** 2011/2016/2021/2024, clause 9.1
- **Status:** Candidate

- **Description:** General information and use case definition Contents: 1 Scope 2 Normative references 3 Terms, definitions and abbreviated terms 3.1 Terms and definitions 3.2 Abbreviated terms 4 Conventions 5 Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parame

---

## iso-15765-9.5 - Flow

- **Official ID:** iso-15765-9.5
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 9.5
- **Source reference:** 2011/2016/2021/2024, clause 9.5
- **Status:** Verified

- **Description:** FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network layer communication protocol for the exchange of data between network nodes, e.g. from ECU to ECU, or between external test equipment and an ECU. If the data to be transferred do not fit into a single CAN frame, a segmentation method is provided. The network layer shall provide services to higher layers. The service interface shall define a set of services. The transport protocol shall support segmentation of messages that exceed the size of a single CAN frame. The flow control shall manage the data flow between sender and receiver. The addressing shall support different addressing formats including normal, normal

---

## iso-15765-10.1 - General

- **Official ID:** iso-15765-10.1
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 10.1
- **Source reference:** 2011/2016/2021/2024, clause 10.1
- **Status:** Candidate

- **Description:** General information and use case definition Contents: 1 Scope 2 Normative references 3 Terms, definitions and abbreviated terms 3.1 Terms and definitions 3.2 Abbreviated terms 4 Conventions 5 Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parame

---

## iso-15765-10.2 - Parameter

- **Official ID:** iso-15765-10.2
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 10.2
- **Source reference:** 2011/2016/2021/2024, clause 10.2
- **Status:** Candidate

- **Description:** Parameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network layer communication protocol for the exchange of data between network nodes, e.g. from ECU to ECU, or between external test equipment and an ECU. If the data to be transferred do not fit into a single CAN frame,

---

## iso-15765-10.2.1 - Timing

- **Official ID:** iso-15765-10.2.1
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 10.2.1
- **Source reference:** 2011/2016/2021/2024, clause 10.2.1
- **Status:** Verified

- **Description:** Timing parameter values 10.2.2 Definition of flow control parameter values 10.2.3 Maximum number of OBDonUDS or OBDonEDS ECUs 10.3 Addressing formats 10.3.1 Normal and normal fixed addressing format 10.3.2 Functional addressing 10.3.3 Physical addressing 10.4 CAN identifier requirements 10.4.1 External test equipment 10.4.2 OBDonUDS or OBDonEDS server/ECU 10.5 Mapping of diagnostic addresses 10.5.1 OBDonUDS/OBDonEDS CAN identifiers 10.5.2 11-bit CAN identifiers 10.5.3 29-bit CAN identifiers 11 Data link layer (DLL) 12 Physical layer (PHY) 12.1 General 12.2 Bit rates ISO 15765-4:2021 specifies the requirements for emissions-related systems. The vehicle communication initialisation sequence shall be performed according to the specified protocol identification procedure. The external test equipment communication initialisation sequence shall be performed before any diagnostic communication. The bit rate validation procedure shall be executed to ensure correct communication. The CAN identifier validation procedure shall be performed for both OBDonEDS and OBDonUDS protocols. The application layer shall provide the diagnostic services. The session layer shall manage the diagnostic session. The transport layer shall provide the transport protocol services. The network layer shall provide the network layer services with the specified timing parameters. The data link layer shall comply with ISO 11898-1. The physical layer shall support the specified bit rates. ===LOCAL_SOURCE=== .. SPDX-License-Identifier: (GPL-2.0 OR BSD-3-Clause) ==================== ISO 15765-2 (ISO-TP) ==================== Overview ======== ISO 15765-2, also known as ISO-TP, is a transport protocol specifically defined for diagnostic communication on CAN. It is widely used in the automotive industry, for example as the transport protocol for UDSonCAN (ISO 14229-3) or emission-related diagnostic services (ISO 15031-5). ISO-TP can be used both on CAN CC (aka Classical CAN) and CAN FD (CAN with Flexible D

---

## iso-15765-10.2.2 - Definition

- **Official ID:** iso-15765-10.2.2
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 10.2.2
- **Source reference:** 2011/2016/2021/2024, clause 10.2.2
- **Status:** Verified

- **Description:** Definition of flow control parameter values 10.2.3 Maximum number of OBDonUDS or OBDonEDS ECUs 10.3 Addressing formats 10.3.1 Normal and normal fixed addressing format 10.3.2 Functional addressing 10.3.3 Physical addressing 10.4 CAN identifier requirements 10.4.1 External test equipment 10.4.2 OBDonUDS or OBDonEDS server/ECU 10.5 Mapping of diagnostic addresses 10.5.1 OBDonUDS/OBDonEDS CAN identifiers 10.5.2 11-bit CAN identifiers 10.5.3 29-bit CAN identifiers 11 Data link layer (DLL) 12 Physical layer (PHY) 12.1 General 12.2 Bit rates ISO 15765-4:2021 specifies the requirements for emissions-related systems. The vehicle communication initialisation sequence shall be performed according to the specified protocol identification procedure. The external test equipment communication initialisation sequence shall be performed before any diagnostic communication. The bit rate validation procedure shall be executed to ensure correct communication. The CAN identifier validation procedure shall be performed for both OBDonEDS and OBDonUDS protocols. The application layer shall provide the diagnostic services. The session layer shall manage the diagnostic session. The transport layer shall provide the transport protocol services. The network layer shall provide the network layer services with the specified timing parameters. The data link layer shall comply with ISO 11898-1. The physical layer shall support the specified bit rates. ===LOCAL_SOURCE=== .. SPDX-License-Identifier: (GPL-2.0 OR BSD-3-Clause) ==================== ISO 15765-2 (ISO-TP) ==================== Overview ======== ISO 15765-2, also known as ISO-TP, is a transport protocol specifically defined for diagnostic communication on CAN. It is widely used in the automotive industry, for example as the transport protocol for UDSonCAN (ISO 14229-3) or emission-related diagnostic services (ISO 15031-5). ISO-TP can be used both on CAN CC (aka Classical CAN) and CAN FD (CAN with Flexible Datarate) based networks. It is

---

## iso-15765-10.3 - Addressing

- **Official ID:** iso-15765-10.3
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 10.3
- **Source reference:** 2011/2016/2021/2024, clause 10.3
- **Status:** Verified

- **Description:** Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network layer communication protocol for the exchange of data between network nodes, e.g. from ECU to ECU, or between external test equipment and an ECU. If the data to be transferred do not fit into a single CAN frame, a segmentation method is provided. The network layer shall provide services to higher layers. The service interface shall define a set of services. The transport protocol shall support segmentation of messages that exceed the size of a single CAN frame. The flow control shall manage the data flow between sender and receiver. The addressing shall support different addressing formats including normal, normal fixed, functional and physical addressing. The timing parameters shall be defined for all protocol operations. The CAN identifier requirements shall be met for both 11-bit and 29-bit identifiers. The data

---

## iso-15765-10.3.3 - Physical

- **Official ID:** iso-15765-10.3.3
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 10.3.3
- **Source reference:** 2011/2016/2021/2024, clause 10.3.3
- **Status:** Verified

- **Description:** Physical addressing 10.4 CAN identifier requirements 10.4.1 External test equipment 10.4.2 OBDonUDS or OBDonEDS server/ECU 10.5 Mapping of diagnostic addresses 10.5.1 OBDonUDS/OBDonEDS CAN identifiers 10.5.2 11-bit CAN identifiers 10.5.3 29-bit CAN identifiers 11 Data link layer (DLL) 12 Physical layer (PHY) 12.1 General 12.2 Bit rates ISO 15765-4:2021 specifies the requirements for emissions-related systems. The vehicle communication initialisation sequence shall be performed according to the specified protocol identification procedure. The external test equipment communication initialisation sequence shall be performed before any diagnostic communication. The bit rate validation procedure shall be executed to ensure correct communication. The CAN identifier validation procedure shall be performed for both OBDonEDS and OBDonUDS protocols. The application layer shall provide the diagnostic services. The session layer shall manage the diagnostic session. The transport layer shall provide the transport protocol services. The network layer shall provide the network layer services with the specified timing parameters. The data link layer shall comply with ISO 11898-1. The physical layer shall support the specified bit rates. ===LOCAL_SOURCE=== .. SPDX-License-Identifier: (GPL-2.0 OR BSD-3-Clause) ==================== ISO 15765-2 (ISO-TP) ==================== Overview ======== ISO 15765-2, also known as ISO-TP, is a transport protocol specifically defined for diagnostic communication on CAN. It is widely used in the automotive industry, for example as the transport protocol for UDSonCAN (ISO 14229-3) or emission-related diagnostic services (ISO 15031-5). ISO-TP can be used both on CAN CC (aka Classical CAN) and CAN FD (CAN with Flexible Datarate) based networks. It is also designed to be compatible with a CAN network using SAE J1939 as data link layer (however, this is not a requirement). Specifications used ------------------- * ISO 15765-2:2024 : Road vehicles - Diag

---

## iso-15765-10.5 - Mapping

- **Official ID:** iso-15765-10.5
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 10.5
- **Source reference:** 2011/2016/2021/2024, clause 10.5
- **Status:** Candidate

- **Description:** Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parameter_Value 8.3.7 Result 8.3.8 Result_ChangeParameter 8.4 ASP T_Data to TL_Data interface mapping 9 PDU structure and protocol control information 9.1 General 9.2 SingleFrame (SF) 9.3 FirstFrame (FF) 9.4 ConsecutiveFrame (CF) 9.5 FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer se

---

## iso-15765-10.6 - Flow

- **Official ID:** iso-15765-10.6
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 10.6
- **Source reference:** 2011/2016/2021/2024, clause 10.6
- **Status:** Verified

- **Description:** FlowControl (FC) 10 Transport and network layer protocol 10.1 General 10.2 Segmented reception 10.3 Segmented transmission 10.4 Reception timeout 10.5 Transmission timeout 10.6 Flow control parameter 10.7 Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network layer communication protocol for the exchange of data between network nodes, e.g. from ECU to ECU, or between external test equipment and an ECU. If the data to be transferred do not fit into a single CAN frame, a segmentation method is provided. The network layer shall provide services to higher layers. The service interface shall define a set of services. The transport protocol shall support segmentation of messages that exceed the size of a single CAN frame. The flow control shall manage the data flow between sender and receiver. The addressing shall support different addressing formats including normal, normal

---

## iso-15765-10.7 - Addressing

- **Official ID:** iso-15765-10.7
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 10.7
- **Source reference:** 2011/2016/2021/2024, clause 10.7
- **Status:** Verified

- **Description:** Addressing 10.8 N_As and N_Bs timers 10.9 N_Ar and N_Br timers 10.10 N_Cs timer 10.11 N_Cr timer 11 Communication flow examples 11.1 General 11.2 Unsegmented communication 11.3 Segmented communication 11.4 Error handling examples ISO 15765-2:2024 specifies a transport and network layer protocol with transport and network layer services tailored to meet the requirements of CAN-based vehicle network systems on controller area networks as specified in ISO 11898-1. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized abstract service primitive interface as specified in ISO 14229-2 (UDS). This document supports different application layer protocols such as enhanced vehicle diagnostics, emissions-related on-board diagnostics (OBD), world-wide harmonized on-board diagnostics (WWH-OBD), and end of life activation of on-board pyrotechnic devices. The transport protocol specifies an unconfirmed communication. The transport protocol and network layer services covered by this part of ISO 15765 have been defined to be independent of the physical layer implemented. This part of ISO 15765 specifies an unconfirmed network layer communication protocol for the exchange of data between network nodes, e.g. from ECU to ECU, or between external test equipment and an ECU. If the data to be transferred do not fit into a single CAN frame, a segmentation method is provided. The network layer shall provide services to higher layers. The service interface shall define a set of services. The transport protocol shall support segmentation of messages that exceed the size of a single CAN frame. The flow control shall manage the data flow between sender and receiver. The addressing shall support different addressing formats including normal, normal fixed, functional and physical addressing. The timing parameters shall be defined for all protocol operations. The CAN identifier requirements shall be met for both 11-bit and 29-bit identifiers. The data

---

## iso-15765-11.1 - General

- **Official ID:** iso-15765-11.1
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 11.1
- **Source reference:** 2011/2016/2021/2024, clause 11.1
- **Status:** Candidate

- **Description:** General information and use case definition Contents: 1 Scope 2 Normative references 3 Terms, definitions and abbreviated terms 3.1 Terms and definitions 3.2 Abbreviated terms 4 Conventions 5 Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parame

---

## iso-15765-12.1 - General

- **Official ID:** iso-15765-12.1
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 12.1
- **Source reference:** 2011/2016/2021/2024, clause 12.1
- **Status:** Candidate

- **Description:** General information and use case definition Contents: 1 Scope 2 Normative references 3 Terms, definitions and abbreviated terms 3.1 Terms and definitions 3.2 Abbreviated terms 4 Conventions 5 Overview of ISO 15765 5.1 General 5.2 Open Systems Interconnection (OSI) model 6 Diagnostic network architecture 6.1 Diagnostic network 6.2 Diagnostic sub-network 6.3 Diagnostic gateway 7 DoCAN use case overview and principles 7.1 Overview 7.2 DoCAN use case clusters 8 DoCAN use case definition 8.1 Use case 1 Vehicle inspection and repair 8.2 Use case 2 Vehicle/ECU software reprogramming 8.3 Use case 3 Vehicle/ECU assembly line inspection and repair ISO 15765-1:2011 gives an overview of the structure and the partitioning of ISO 15765, and shows the relationships between the different parts. It also defines the diagnostic network architecture. The terminology defined in this part is common for all diagnostic networks and is used throughout all parts of ISO 15765. The diagnostic communication over controller area network (DoCAN) protocol supports the standardized service primitive interface as specified in ISO 14229-2. ISO 15765-2:2024 Part 2: Transport protocol and network layer services Contents: 1 Scope 2 Normative references 3 Terms and definitions 4 Symbols and abbreviated terms 4.1 Symbols 4.2 Abbreviated terms 5 Conventions 6 ISO 11898-1 CAN data link layer extension 6.1 CAN CC and CAN FD frame feature comparison 6.2 Mapping of transport and network layer attributes to CAN data frames 7 T_Data abstract service primitive interface definition 7.1 T_Data services 7.2 T_Data interface 7.3 Data type definitions 8 Transport and network layer services 8.1 General 8.2 Transport and network layer abstract service primitives 8.2.1 Data.req 8.2.2 Data.con 8.2.3 Data_FF.ind 8.2.4 Data.ind 8.2.5 ChangeParameter.req 8.2.6 ChangeParameter.con 8.3 Service data unit specification 8.3.1 Mtype, message type 8.3.2 AI, address information 8.3.3 N_AI 8.3.4 Mtype 8.3.5 Parameter 8.3.6 Parame

---

## iso-15765-12.2 - Bit rate

- **Official ID:** iso-15765-12.2
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause 12.2
- **Source reference:** 2011/2016/2021/2024, clause 12.2
- **Status:** Verified

- **Description:** Bit rate validation procedure 6.3.1 bitrateRecord 6.3.2 Bit rate validation 6.3.3 External test equipment error detection provisions 6.4 CAN identifier validation procedure 6.4.1 CAN identifier validation procedure OBDonEDS 6.4.2 CAN identifier validation procedure OBDonUDS 6.5 Support of ECUNAME reporting 7 Application layer (AL) 8 Session layer (SL) 9 Transport layer (TL) 10 Network layer (NL) 10.1 General 10.2 Parameter definitions 10.2.1 Timing parameter values 10.2.2 Definition of flow control parameter values 10.2.3 Maximum number of OBDonUDS or OBDonEDS ECUs 10.3 Addressing formats 10.3.1 Normal and normal fixed addressing format 10.3.2 Functional addressing 10.3.3 Physical addressing 10.4 CAN identifier requirements 10.4.1 External test equipment 10.4.2 OBDonUDS or OBDonEDS server/ECU 10.5 Mapping of diagnostic addresses 10.5.1 OBDonUDS/OBDonEDS CAN identifiers 10.5.2 11-bit CAN identifiers 10.5.3 29-bit CAN identifiers 11 Data link layer (DLL) 12 Physical layer (PHY) 12.1 General 12.2 Bit rates ISO 15765-4:2021 specifies the requirements for emissions-related systems. The vehicle communication initialisation sequence shall be performed according to the specified protocol identification procedure. The external test equipment communication initialisation sequence shall be performed before any diagnostic communication. The bit rate validation procedure shall be executed to ensure correct communication. The CAN identifier validation procedure shall be performed for both OBDonEDS and OBDonUDS protocols. The application layer shall provide the diagnostic services. The session layer shall manage the diagnostic session. The transport layer shall provide the transport protocol services. The network layer shall provide the network layer services with the specified timing parameters. The data link layer shall comply with ISO 11898-1. The physical layer shall support the specified bit rates. ===LOCAL_SOURCE=== .. SPDX-License-Identifier: (GPL-2.0 OR BSD-3-Clause) ===

---

## iso-15765-REQ20 - CAN ID plus the first byte of the CAN payload; both the CAN ID and the byte insi...

- **Official ID:** iso-15765-REQ20
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause REQ20 (clause 12)
- **Source reference:** 2011/2016/2021/2024, clause REQ20 (clause 12)
- **Status:** Verified

- **Description:** CAN ID plus the first byte of the CAN payload; both the CAN ID and the byte inside the payload shall be different between two addresses.

---

## iso-15765-REQ21 - Once this information has been received, the sender starts to send frames contai...

- **Official ID:** iso-15765-REQ21
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause REQ21 (clause 12)
- **Source reference:** 2011/2016/2021/2024, clause REQ21 (clause 12)
- **Status:** Verified

- **Description:** Once this information has been received, the sender starts to send frames containing fragments of the data payload (called Consecutive Frames - CF), stopping after every ``blocksize``-sized block to wait confirmation from the receiver which should then send another Flow Control frame to inform the sender about its availability to receive more data.

---

## iso-15765-REQ22 - Creation and basic usage of an ISO-TP socket -----------------------------------...

- **Official ID:** iso-15765-REQ22
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause REQ22 (clause 12)
- **Source reference:** 2011/2016/2021/2024, clause REQ22 (clause 12)
- **Status:** Verified

- **Description:** Creation and basic usage of an ISO-TP socket -------------------------------------------- To use the ISO-TP stack, ``#include `` shall be used.

---

## iso-15765-REQ23 - C s = socket(PF_CAN, SOCK_DGRAM, CAN_ISOTP); After the socket has been successfu...

- **Official ID:** iso-15765-REQ23
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause REQ23 (clause 12)
- **Source reference:** 2011/2016/2021/2024, clause REQ23 (clause 12)
- **Status:** Verified

- **Description:** C s = socket(PF_CAN, SOCK_DGRAM, CAN_ISOTP); After the socket has been successfully created, ``bind(2)`` shall be called to bind the socket to the desired CAN interface; to do so: * a TX CAN ID shall be specified as part of the sockaddr supplied to the call itself.

---

## iso-15765-REQ24 - RX CAN ID shall also be specified, unless broadcast flags have been set through ...

- **Official ID:** iso-15765-REQ24
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause REQ24 (clause 12)
- **Source reference:** 2011/2016/2021/2024, clause REQ24 (clause 12)
- **Status:** Verified

- **Description:** RX CAN ID shall also be specified, unless broadcast flags have been set through socket option (explained below).

---

## iso-15765-REQ25 - To set the transmission time to ``0``, the ``CAN_ISOTP_FRAME_TXTIME_ZERO`` macro...

- **Official ID:** iso-15765-REQ25
- **Standard / Version:** ISO 15765 Road vehicles Diagnostic communication over Controller Area Network (DoCAN) 2011/2016/2021/2024
- **Category:** Clause REQ25 (clause 12)
- **Source reference:** 2011/2016/2021/2024, clause REQ25 (clause 12)
- **Status:** Verified

- **Description:** To set the transmission time to ``0``, the ``CAN_ISOTP_FRAME_TXTIME_ZERO`` macro (equal to 0xFFFFFFFF) shall be used.

---

## Limitations and Open Questions

- The source content was extracted from PDF text extraction and/or web content parsing.
- 51 requirements extracted from 45 detected clauses.
- Requirements containing requirement keywords (shall, should, must) are marked Verified.
- Other clauses are marked Candidate as they may contain normative content not captured by keyword detection.
- Source: https://cdn.standards.iteh.ai/samples/54499/2a977e03a16341ef904152ef97a0d74b/ISO-15765-2-2011.pdf (downloaded 2026-09-09).
- Additional web sources:
  - https://www.kernel.org/doc/Documentation/networking/iso15765-2.rst
