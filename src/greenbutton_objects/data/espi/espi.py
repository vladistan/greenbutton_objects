from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict
from xsdata_pydantic.fields import field

__NAMESPACE__ = "http://naesb.org/espi"


class AccumulationKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable or implied by the unit of measure.
    :cvar VALUE_1: A value from a register which represents the bulk
        quantity of a commodity. This quantity is computed as the
        integral of the commodity usage rate. This value is typically
        used as the basis for the dial reading at the meter, and as a
        result, will roll over upon reaching a maximum dial value. Note
        1: With the metering system, the roll-over behavior typically
        implies a roll-under behavior so that the value presented is
        always a positive value (e.g. unsigned integer or positive
        decimal.) However, when communicating data between enterprise
        applications a negative value might occur in a case such as net
        metering. Note 2: A BulkQuantity refers primarily to the dial
        reading and not the consumption over a specific period of time.
    :cvar VALUE_2: The sum of the previous billing period values and the
        present period value. Note: “ContinuousCumulative” is commonly
        used in conjunction with “demand.” The “ContinuousCumulative
        Demand” would be the cumulative sum of the previous billing
        period maximum demand values (as occurring with each demand
        reset) summed with the present period maximum demand value
        (which has yet to be reset.)
    :cvar VALUE_3: The sum of the previous billing period values. Note:
        “Cumulative” is commonly used in conjunction with “demand.” Each
        demand reset causes the maximum demand value for the present
        billing period (since the last demand reset) to accumulate as an
        accumulative total of all maximum demands. So instead of
        “zeroing” the demand register, a demand reset has the effect of
        adding the present maximum demand to this accumulating total.
    :cvar VALUE_4: The difference between the value at the end of the
        prescribed interval and the beginning of the interval. This is
        used for incremental interval data. Note: One common application
        would be for load profile data, another use might be to report
        the number of events within an interval (such as the number of
        equipment energizations within the specified period of time.)
    :cvar VALUE_6: As if a needle is swung out on the meter face to a
        value to indicate the current value. (Note: An “indicating”
        value is typically measured over hundreds of milliseconds or
        greater, or may imply a “pusher” mechanism to capture a value.
        Compare this to “instantaneous” which is measured over a shorter
        period of time.)
    :cvar VALUE_9: A form of accumulation which is selective with
        respect to time. Note : “Summation” could be considered a
        specialization of “Bulk Quantity” according to the rules of
        inheritance where “Summation” selectively accumulates pulses
        over a timing pattern, and “BulkQuantity” accumulates pulses all
        of the time.
    :cvar VALUE_10: A form of computation which introduces a time delay
        characteristic to the data value
    :cvar VALUE_12: Typically measured over the fastest period of time
        allowed by the definition of the metric (usually milliseconds or
        tens of milliseconds.) (Note: “Instantaneous” was moved to
        attribute #3 in 61968-9Ed2 from attribute #1 in 61968-9Ed1.)
    :cvar VALUE_13: When this description is applied to a metered value,
        it implies that the value is a time-independent cumulative
        quantity much a BulkQuantity, except that it latches upon the
        maximum value upon reaching that value. Any additional
        accumulation (positive or negative) is discarded until a reset
        occurs. Note: A LatchingQuantity may also occur in the downward
        direction – upon reaching a minimum value. The terms “maximum”
        or “minimum” will usually be included as an attribute when this
        type of accumulation behavior is present. When this description
        is applied to an encoded value (UOM= “Code”), it implies that
        the value has one or more bits which are latching. The condition
        that caused the bit to be set may have long since evaporated. In
        either case, the timestamp that accompanies the value may not
        coincide with the moment the value was initially set. In both
        cases a system will need to perform an operation to clear the
        latched value.
    :cvar VALUE_14: A time-independent cumulative quantity much a
        BulkQuantity or a LatchingQuantity, except that the accumulation
        stops at the maximum or minimum values. When the maximum is
        reached, any additional positive accumulation is discarded, but
        negative accumulation may be accepted (thus lowering the
        counter.) Likewise, when the negative bound is reached, any
        additional negative accumulation is discarded, but positive
        accumulation is accepted (thus increasing the counter.)
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_6 = 6
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14


class AmiBillingReadyKind(Enum):
    """
    Lifecycle states of the metering installation at a usage point with respect to
    readiness for billing via advanced metering infrastructure reads.

    :cvar AMI_CAPABLE: Usage point is equipped with an AMI capable meter
        that is not yet currently equipped with a communications module.
    :cvar AMI_DISABLED: Usage point is equipped with an AMI capable
        meter; however, the AMI functionality has been disabled or is
        not being used.
    :cvar BILLING_APPROVED: Usage point is equipped with an operating
        AMI capable meter and accuracy has been certified for billing
        purposes.
    :cvar ENABLED: Usage point is equipped with an AMI capable meter
        having communications capability.
    :cvar NON_AMI: Usage point is equipped with a non AMI capable meter.
    :cvar NON_METERED: Usage point is not currently equipped with a
        meter.
    :cvar OPERABLE: Usage point is equipped with an AMI capable meter
        that is functioning and communicating with the AMI network.
    """

    AMI_CAPABLE = "amiCapable"
    AMI_DISABLED = "amiDisabled"
    BILLING_APPROVED = "billingApproved"
    ENABLED = "enabled"
    NON_AMI = "nonAmi"
    NON_METERED = "nonMetered"
    OPERABLE = "operable"


class AnodeType(Enum):
    """Aggregated Nodes Types for example:
    - SYS - System Zone/Region;
    - RUC - RUC Zone;
    - LFZ - Load Forecast Zone;
    - REG - Market Energy/Ancillary Service Region;
    - AGR - Aggregate Generation Resource;
    - POD - Point of Delivery;
    - ALR - Aggregate Load Resource;
    - LTAC - Load TransmissionAccessCharge (TAC) Group;
    - ACA - Adjacent Control Area
    - ASR - Aggregated System Resource
    - ECA - Embedded Control Area

    :cvar SYS: System Zone/Region;
    :cvar RUC: RUC Zone
    :cvar LFZ: Load Forecast Zone
    :cvar REG: Market Energy/Ancillary Service Region;
    :cvar AGR: Aggregate Generation Resource;
    :cvar POD: Point of Delivery;
    :cvar ALR: Aggregate Load Resource;
    :cvar LTAC: Load TransmissionAccessCharge (TAC) Group;
    :cvar ACA: Adjacent Control Area
    :cvar ASR: Aggregated System Resource
    :cvar ECA: Embedded Control Area
    """

    SYS = "SYS"
    RUC = "RUC"
    LFZ = "LFZ"
    REG = "REG"
    AGR = "AGR"
    POD = "POD"
    ALR = "ALR"
    LTAC = "LTAC"
    ACA = "ACA"
    ASR = "ASR"
    ECA = "ECA"


class ApnodeType(Enum):
    """Aggregate Node Types for example:
    AG -  Aggregated Generation
    CPZ -  Custom Price Zone
    DPZ -  Default Price Zone
    LAP - Load Aggregation Point
    TH -  Trading  Hub
    SYS - System Zone
    CA - Control Area
    GA - generic aggregation
    EHV - 500 kV
    GH - generic hub
    ZN - zone
    INT - Interface
    BUS - Bus

    :cvar AG: Aggregated Generation
    :cvar CPZ: Custom Price Zone
    :cvar DPZ: Default Price Zone
    :cvar LAP: Load Aggregation Point
    :cvar TH: Trading  Hub
    :cvar SYS: System Zone
    :cvar CA: Control Area
    :cvar DCA: Designated Congestion Area
    :cvar GA: generic aggregation
    :cvar GH: generic hub
    :cvar EHV: 500 kV - Extra High Voltage aggregate price nodes
    :cvar ZN: Zone
    :cvar INT: Interface
    :cvar BUS: Bus
    """

    AG = "AG"
    CPZ = "CPZ"
    DPZ = "DPZ"
    LAP = "LAP"
    TH = "TH"
    SYS = "SYS"
    CA = "CA"
    DCA = "DCA"
    GA = "GA"
    GH = "GH"
    EHV = "EHV"
    ZN = "ZN"
    INT = "INT"
    BUS = "BUS"


class AuthorizationStatusValue(Enum):
    """
    :cvar VALUE_0: Revoked
    :cvar VALUE_1: Active
    :cvar VALUE_2: Denied
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


class BatchListType(BaseModel):
    """
    [extension] List of resource URIs that can be used to GET ESPI resources.

    :ivar resources: An individual resource URI.
    """

    model_config = ConfigDict(defer_build=True)
    resources: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )


class CrudoperationValue(Enum):
    """
    :cvar VALUE_0: Create
    :cvar VALUE_1: Read
    :cvar VALUE_2: Update
    :cvar VALUE_3: Delete
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class CommodityKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_1: All types of metered quantities. This type of reading
        comes from the meter and represents a “secondary” metered value.
    :cvar VALUE_2: It is possible for a meter to be outfitted with an
        external VT and/or CT. The meter might not be aware of these
        devices, and the display not compensate for their presence.
        Ultimately, when these scalars are applied, the value that
        represents the service value is called the “primary metered”
        value. The “index” in sub-category 3 mirrors those of sub-
        category 0.
    :cvar VALUE_3: A measurement of the communication infrastructure
        itself.
    :cvar VALUE_4: Air
    :cvar VALUE_5: Insulative Gas (SF6 is found separately below)
    :cvar VALUE_6: Insulative Oil
    :cvar VALUE_7: Natural Gas
    :cvar VALUE_8: Propane C3H8
    :cvar VALUE_9: Drinkable water
    :cvar VALUE_10: Water in steam form, usually used for heating.
    :cvar VALUE_11: Waste Water (Sewerage)
    :cvar VALUE_12: This fluid is likely in liquid form. It is not
        necessarily water or water based. The warm fluid returns cooler
        than when it was sent. The heat conveyed may be metered.
    :cvar VALUE_13: The cool fluid returns warmer than when it was sent.
        The heat conveyed may be metered.
    :cvar VALUE_14: Reclaimed water – possibly used for irrigation but
        not sufficiently treated to be considered safe for drinking.
    :cvar VALUE_15: Nitrous Oxides NOX
    :cvar VALUE_16: Sulfur Dioxide SO2
    :cvar VALUE_17: Methane CH4
    :cvar VALUE_18: Carbon Dioxide CO2
    :cvar VALUE_19: Carbon
    :cvar VALUE_20: Hexachlorocyclohexane HCH
    :cvar VALUE_21: Perfluorocarbons PFC
    :cvar VALUE_22: Sulfurhexafluoride SF6
    :cvar VALUE_23: Television
    :cvar VALUE_24: Internet service
    :cvar VALUE_25: Trash
    :cvar VALUE_26: Electricity Transmission "metered" -- Service taken
        directly from transmission system without transformation from
        standard transmission voltages
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26


class CurrencyValue(Enum):
    """
    :cvar VALUE_840: US dollar
    :cvar VALUE_978: European euro
    :cvar VALUE_36: Australian dollar
    :cvar VALUE_124: Canadian dollar
    :cvar VALUE_756: Swiss francs
    :cvar VALUE_156: Chinese yuan renminbi
    :cvar VALUE_208: Danish crown
    :cvar VALUE_826: British pound
    :cvar VALUE_392: Japanese yen
    :cvar VALUE_578: Norwegian crown
    :cvar VALUE_643: Russian ruble
    :cvar VALUE_752: Swedish crown
    :cvar VALUE_356: India rupees
    :cvar VALUE_0: Another type of currency.
    """

    VALUE_840 = 840
    VALUE_978 = 978
    VALUE_36 = 36
    VALUE_124 = 124
    VALUE_756 = 756
    VALUE_156 = 156
    VALUE_208 = 208
    VALUE_826 = 826
    VALUE_392 = 392
    VALUE_578 = 578
    VALUE_643 = 643
    VALUE_752 = 752
    VALUE_356 = 356
    VALUE_0 = 0


class DataCustodianApplicationStatusValue(Enum):
    """
    :cvar VALUE_1: Review
    :cvar VALUE_2: Production (Live)
    :cvar VALUE_3: On Hold
    :cvar VALUE_4: Revoked
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class DataQualifierKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_2: Average value
    :cvar VALUE_4: The value represents an amount over which a threshold
        was exceeded.
    :cvar VALUE_5: The value represents a programmed threshold.
    :cvar VALUE_7: The value represents a programmed threshold.
    :cvar VALUE_8: The highest value observed
    :cvar VALUE_9: The smallest value observed
    :cvar VALUE_11: Nominal
    :cvar VALUE_12: Normal
    :cvar VALUE_16: The second highest value observed
    :cvar VALUE_17: The second smallest value observed
    :cvar VALUE_23: The third highest value observed
    :cvar VALUE_24: The fourth highest value observed
    :cvar VALUE_25: The fifth highest value observed
    :cvar VALUE_26: The accumulated sum
    """

    VALUE_0 = 0
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26


class EspiserviceStatusValue(Enum):
    """
    :cvar VALUE_0: Unavailable
    :cvar VALUE_1: Normal; operational
    """

    VALUE_0 = 0
    VALUE_1 = 1


class EnrollmentStatus(Enum):
    """
    [extension] Current Tariff Rider enrollment status.

    :cvar UNENROLLED: Currently NOT enrolled in Tariff Rider
    :cvar ENROLLED: Currently enrolled in the Tariff Rider
    :cvar ENROLLED_PENDING: Currently pending enrollment in Tariff Rider
    """

    UNENROLLED = "unenrolled"
    ENROLLED = "enrolled"
    ENROLLED_PENDING = "enrolledPending"


class FlowDirectionKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable (N/A)
    :cvar VALUE_1: "Delivered," or "Imported" as defined 61968-2.Forward
        Active Energy is a positive kWh value as one would naturally
        expect to find as energy is supplied by the utility and consumed
        at the service. Forward Reactive Energy is a positive VArh value
        as one would naturally expect to find in the presence of
        inductive loading. In polyphase metering, the forward energy
        register is incremented when the sum of the phase energies is
        greater than zero.
    :cvar VALUE_2: Typically used to describe that a power factor is
        lagging the reference value. Note 1: When used to describe VA,
        “lagging” describes a form of measurement where reactive power
        is considered in all four quadrants, but real power is
        considered only in quadrants I and IV. Note 2: When used to
        describe power factor, the term “Lagging” implies that the PF is
        negative. The term “lagging” in this case takes the place of the
        negative sign. If a signed PF value is to be passed by the data
        producer, then the direction of flow enumeration zero (none)
        should be used in order to avoid the possibility of creating an
        expression that employs a double negative. The data consumer
        should be able to tell from the sign of the data if the PF is
        leading or lagging. This principle is analogous to the concept
        that “Reverse” energy is an implied negative value, and to
        publish a negative reverse value would be ambiguous. Note 3:
        Lagging power factors typically indicate inductive loading.
    :cvar VALUE_3: Typically used to describe that a power factor is
        leading the reference value. Note: Leading power factors
        typically indicate capacitive loading.
    :cvar VALUE_4: |Forward| - |Reverse|, See 61968-2.Note: In some
        systems, the value passed as a “net” value could become
        negative. In other systems the value passed as a “net” value is
        always a positive number, and rolls-over and rolls-under as
        needed.
    :cvar VALUE_5: Reactive positive quadrants. (The term “lagging” is
        preferred.)
    :cvar VALUE_7: Quadrants 1 and 3
    :cvar VALUE_8: Quadrants 1 and 4 usually represent forward active
        energy
    :cvar VALUE_9: Q1 minus Q4
    :cvar VALUE_10: Quadrants 2 and 3 usually represent reverse active
        energy
    :cvar VALUE_11: Quadrants 2 and 4
    :cvar VALUE_12: Q2 minus Q3
    :cvar VALUE_13: Reactive negative quadrants. (The term “leading” is
        preferred.)
    :cvar VALUE_14: Q3 minus Q2
    :cvar VALUE_15: Q1 only
    :cvar VALUE_16: Q2 only
    :cvar VALUE_17: Q3 only
    :cvar VALUE_18: Q4 only
    :cvar VALUE_19: Reverse Active Energy is equivalent to "Received,"
        or "Exported" as defined in 61968-2. Reverse Active Energy is a
        positive kWh value as one would expect to find when energy is
        backfed by the service onto the utility network. Reverse
        Reactive Energy is a positive VArh value as one would expect to
        find in the presence of capacitive loading and a leading Power
        Factor. In polyphase metering, the reverse energy register is
        incremented when the sum of the phase energies is less than
        zero. Note: The value passed as a reverse value is always a
        positive value. It is understood by the label “reverse” that it
        represents negative flow.
    :cvar VALUE_20: |Forward| + |Reverse|, See 61968-2. The sum of the
        commodity in all quadrants Q1+Q2+Q3+Q4. In polyphase metering,
        the total energy register is incremented when the absolute value
        of the sum of the phase energies is greater than zero.
    :cvar VALUE_21: In polyphase metering, the total by phase energy
        register is incremented when the sum of the absolute values of
        the phase energies is greater than zero. In single phase
        metering, the formulas for “Total” and “Total by phase” collapse
        to the same expression. For communication purposes however, the
        “Total” enumeration should be used with single phase meter data.
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21


class GrantType(Enum):
    """
    [extension] OAuth 2.0 ESPI supported grant types.

    :cvar AUTHORIZATION_CODE: OAuth 2.0 Authorization Code Grant flow
        (RFC 6749 Section 4.1).
    :cvar CLIENT_CREDENTIALS: OAuth 2.0 Client Credentials Grant flow
        (RFC 6749 Section 4.4).
    :cvar REFRESH_TOKEN: OAuth 2.0 Refresh Token flow (RFC 6749 Section
        6.).
    """

    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_CREDENTIALS = "client_credentials"
    REFRESH_TOKEN = "refresh_token"


class ItemKindValue(Enum):
    """
    :cvar VALUE_1: Energy Generation Fee. A charge for generation of
        energy.
    :cvar VALUE_2: Energy Delivery Fee. A charge for delivery of energy.
    :cvar VALUE_3: Energy Usage Fee. A charge for electricity, natural
        gas, water consumption
    :cvar VALUE_4: Administrative Fee. A fee for administrative
        services.
    :cvar VALUE_5: Tax. A local, state, or federal energy tax.
    :cvar VALUE_6: Energy Generation Credit. A credit, discount or
        rebate for generation of energy.
    :cvar VALUE_7: Energy Delivery Credit. A credit, discount or rebate
        for delivery of energy.
    :cvar VALUE_8: Administrative Credit. A credit, discount or rebate
        for administrative services.
    :cvar VALUE_9: Payment. A payment for a previous billing.
    :cvar VALUE_10: Information. An informational line item.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10


class MeasurementKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_2: Apparent Power Factor
    :cvar VALUE_3: Currency
    :cvar VALUE_4: Current
    :cvar VALUE_5: Current Angle
    :cvar VALUE_6: Current Imbalance
    :cvar VALUE_7: Date
    :cvar VALUE_8: Demand
    :cvar VALUE_9: Distance
    :cvar VALUE_10: Distortion Volt Amperes
    :cvar VALUE_11: Energization
    :cvar VALUE_12: Energy
    :cvar VALUE_13: Energization Load Side
    :cvar VALUE_14: Fan
    :cvar VALUE_15: Frequency
    :cvar VALUE_16: Funds (Duplication of “currency”)
    :cvar VALUE_17: ieee1366ASAI
    :cvar VALUE_18: ieee1366ASIDI
    :cvar VALUE_19: ieee1366ASIFI
    :cvar VALUE_20: ieee1366CAIDI
    :cvar VALUE_21: ieee1366CAIFI
    :cvar VALUE_22: ieee1366CEMIn
    :cvar VALUE_23: ieee1366CEMSMIn
    :cvar VALUE_24: ieee1366CTAIDI
    :cvar VALUE_25: ieee1366MAIFI
    :cvar VALUE_26: ieee1366MAIFIe
    :cvar VALUE_27: ieee1366SAIDI
    :cvar VALUE_28: ieee1366SAIFI
    :cvar VALUE_31: Line Losses
    :cvar VALUE_32: Losses
    :cvar VALUE_33: Negative Sequence
    :cvar VALUE_34: Phasor Power Factor
    :cvar VALUE_35: Phasor Reactive Power
    :cvar VALUE_36: Positive Sequence
    :cvar VALUE_37: Power
    :cvar VALUE_38: Power Factor
    :cvar VALUE_40: Quantity Power
    :cvar VALUE_41: Sag (Voltage Dip)
    :cvar VALUE_42: Swell
    :cvar VALUE_43: Switch Position
    :cvar VALUE_44: Tap Position
    :cvar VALUE_45: Tariff Rate
    :cvar VALUE_46: Temperature
    :cvar VALUE_47: Total Harmonic Distortion
    :cvar VALUE_48: Transformer Losses
    :cvar VALUE_49: Unipede Voltage Dip 10 to 15
    :cvar VALUE_50: Unipede Voltage Dip 15 to 30
    :cvar VALUE_51: Unipede Voltage Dip 30 to 60
    :cvar VALUE_52: Unipede Voltage Dip 60 to 90
    :cvar VALUE_53: Unipede Voltage Dip 90 to 100
    :cvar VALUE_54: Voltage
    :cvar VALUE_55: Voltage Angle
    :cvar VALUE_56: Voltage Excursion
    :cvar VALUE_57: Voltage Imbalance
    :cvar VALUE_58: Volume (Clarified from Ed. 1. to indicate fluid
        volume)
    :cvar VALUE_59: Zero Flow Duration
    :cvar VALUE_60: Zero Sequence
    :cvar VALUE_64: Distortion Power Factor
    :cvar VALUE_81: Frequency Excursion (Usually expressed as a “count”)
    :cvar VALUE_90: Application Context
    :cvar VALUE_91: Ap Title
    :cvar VALUE_92: Asset Number
    :cvar VALUE_93: Bandwidth
    :cvar VALUE_94: Battery Voltage
    :cvar VALUE_95: Broadcast Address
    :cvar VALUE_96: Device Address Type 1
    :cvar VALUE_97: Device Address Type 2
    :cvar VALUE_98: Device Address Type 3
    :cvar VALUE_99: Device Address Type 4
    :cvar VALUE_100: Device Class
    :cvar VALUE_101: Electronic Serial Number
    :cvar VALUE_102: End Device ID
    :cvar VALUE_103: Group Address Type 1
    :cvar VALUE_104: Group Address Type 2
    :cvar VALUE_105: Group Address Type 3
    :cvar VALUE_106: Group Address Type 4
    :cvar VALUE_107: IP Address
    :cvar VALUE_108: MAC Address
    :cvar VALUE_109: Mfg Assigned Configuration ID
    :cvar VALUE_110: Mfg Assigned Physical Serial Number
    :cvar VALUE_111: Mfg Assigned Product Number
    :cvar VALUE_112: Mfg Assigned Unique Communication Address
    :cvar VALUE_113: Multicast Address
    :cvar VALUE_114: One Way Address
    :cvar VALUE_115: Signal Strength
    :cvar VALUE_116: Two Way Address
    :cvar VALUE_117: Signal to Noise Ratio (moved here from Attribute #9
        UOM)
    :cvar VALUE_118: Alarm
    :cvar VALUE_119: Battery Carryover
    :cvar VALUE_120: Data Overflow Alarm
    :cvar VALUE_121: Demand Limit
    :cvar VALUE_122: Demand Reset (usually expressed as a count as part
        of a billing cycle)
    :cvar VALUE_123: Diagnostic
    :cvar VALUE_124: Emergency Limit
    :cvar VALUE_125: Encoder Tamper
    :cvar VALUE_126: ieee1366 Momentary Interruption
    :cvar VALUE_127: ieee1366 Momentary Interruption Event
    :cvar VALUE_128: ieee1366 Sustained Interruption
    :cvar VALUE_129: Interruption Behaviour
    :cvar VALUE_130: Inversion Tamper
    :cvar VALUE_131: Load Interrupt
    :cvar VALUE_132: Load Shed
    :cvar VALUE_133: Maintenance
    :cvar VALUE_134: Physical Tamper
    :cvar VALUE_135: Power Loss Tamper
    :cvar VALUE_136: Power Outage
    :cvar VALUE_137: Power Quality
    :cvar VALUE_138: Power Restoration
    :cvar VALUE_139: Programmed
    :cvar VALUE_140: Push Button
    :cvar VALUE_141: Relay Activation
    :cvar VALUE_142: Relay Cycle (usually expressed as a count)
    :cvar VALUE_143: Removal Tamper
    :cvar VALUE_144: Reprogramming Tamper
    :cvar VALUE_145: Reverse Rotation Tamper
    :cvar VALUE_146: Switch Armed
    :cvar VALUE_147: Switch Disabled
    :cvar VALUE_148: Tamper
    :cvar VALUE_149: Watchdog Timeout
    :cvar VALUE_150: Customer’s bill for the previous billing period
        (Currency)
    :cvar VALUE_151: Customer’s bill, as known thus far within the
        present billing period (Currency)
    :cvar VALUE_152: Customer’s bill for the (Currency)
    :cvar VALUE_153: Monthly fee for connection to commodity.
    :cvar VALUE_154: Audible Volume (Sound)
    :cvar VALUE_155: Volumetric Flow
    """

    VALUE_0 = 0
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_22 = 22
    VALUE_23 = 23
    VALUE_24 = 24
    VALUE_25 = 25
    VALUE_26 = 26
    VALUE_27 = 27
    VALUE_28 = 28
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_33 = 33
    VALUE_34 = 34
    VALUE_35 = 35
    VALUE_36 = 36
    VALUE_37 = 37
    VALUE_38 = 38
    VALUE_40 = 40
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_45 = 45
    VALUE_46 = 46
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_49 = 49
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_56 = 56
    VALUE_57 = 57
    VALUE_58 = 58
    VALUE_59 = 59
    VALUE_60 = 60
    VALUE_64 = 64
    VALUE_81 = 81
    VALUE_90 = 90
    VALUE_91 = 91
    VALUE_92 = 92
    VALUE_93 = 93
    VALUE_94 = 94
    VALUE_95 = 95
    VALUE_96 = 96
    VALUE_97 = 97
    VALUE_98 = 98
    VALUE_99 = 99
    VALUE_100 = 100
    VALUE_101 = 101
    VALUE_102 = 102
    VALUE_103 = 103
    VALUE_104 = 104
    VALUE_105 = 105
    VALUE_106 = 106
    VALUE_107 = 107
    VALUE_108 = 108
    VALUE_109 = 109
    VALUE_110 = 110
    VALUE_111 = 111
    VALUE_112 = 112
    VALUE_113 = 113
    VALUE_114 = 114
    VALUE_115 = 115
    VALUE_116 = 116
    VALUE_117 = 117
    VALUE_118 = 118
    VALUE_119 = 119
    VALUE_120 = 120
    VALUE_121 = 121
    VALUE_122 = 122
    VALUE_123 = 123
    VALUE_124 = 124
    VALUE_125 = 125
    VALUE_126 = 126
    VALUE_127 = 127
    VALUE_128 = 128
    VALUE_129 = 129
    VALUE_130 = 130
    VALUE_131 = 131
    VALUE_132 = 132
    VALUE_133 = 133
    VALUE_134 = 134
    VALUE_135 = 135
    VALUE_136 = 136
    VALUE_137 = 137
    VALUE_138 = 138
    VALUE_139 = 139
    VALUE_140 = 140
    VALUE_141 = 141
    VALUE_142 = 142
    VALUE_143 = 143
    VALUE_144 = 144
    VALUE_145 = 145
    VALUE_146 = 146
    VALUE_147 = 147
    VALUE_148 = 148
    VALUE_149 = 149
    VALUE_150 = 150
    VALUE_151 = 151
    VALUE_152 = 152
    VALUE_153 = 153
    VALUE_154 = 154
    VALUE_155 = 155


class OauthError(Enum):
    """
    [extension] OAuth 2.0 ESPI supported error codes.

    :cvar INVALID_REQUEST: The request is missing a required parameter,
        includes an unsupported parameter value (other than grant type),
        repeats a parameter, includes multiple credentials, utilizes
        more than one mechanism for authenticating the client, or is
        otherwise malformed (RFC 6749 Sections 4.1.2.1 and 5.2).
    :cvar INVALID_CLIENT: Client authentication failed (e.g., unknown
        client, no client authentication included, or unsupported
        authentication method).  The authorization server MAY return an
        HTTP 401 (Unauthorized) status code to indicate which HTTP
        authentication schemes are supported.  If the client attempted
        to authenticate via the Authorization request header field, the
        authorization server MUST respond with an HTTP 401
        (Unauthorized) status code and include the WWW-Authenticate
        response header field matching the authentication scheme used by
        the client. (RFC 6749 Section 5.2).
    :cvar INVALID_GRANT: The provided authorization code or refresh
        token is invalid, expired, revoked, does not match the
        redirection URI used in the authorization request, or was issued
        to another client (RFC 6749 Section 5.2).
    :cvar UNAUTHORIZED_CLIENT: The authenticated client is not
        authorized to use this authorization grant type (RFC 6749
        Sections 4.1.2.1 and 5.2).
    :cvar UNSUPPORTED_GRANT_TYPE: The authorization grant type is not
        supported by the authorization server  (RFC 6749 Section 5.2).
    :cvar INVALID_SCOPE: The requested scope is invalid, unknown,
        malformed, or exceeds the scope granted by the resource owner
        (RFC 6749 Sections 4.1.2.1 and 5.2).
    :cvar INVALID_REDIRECT_URI: The value of one or more redirection
        URIs is invalid (RFC 7591 Section 3.2.2).
    :cvar INVALID_CLIENT_METADATA: The value of one of the client
        metadata fields is invalid and server has rejected the request.
        Not that an authorization server MAY choose to substitute a
        valid value for any requested parameter of a client's metadata
        (RFC 7591 Section 3.2.2).
    :cvar INVALID_CLIENT_ID: [DEPRECATED] Client authentication failed
        (e.g., unknown client, no client authentication included, or
        unsupported authentication method).  The authorization server
        MAY return an HTTP 401 (Unauthorized) status code to indicate
        which HTTP authentication schemes are supported.  If the client
        attempted to authenticate via the Authorization request header
        field, the authorization server MUST respond with an HTTP 401
        (Unauthorized) status code and include the WWW-Authenticate
        response header field matching the authentication scheme used by
        the client.
    :cvar ACCESS_DENIED: The resource owner or authorization server
        denied the request (RFC 6749 Section 4.1.2.1).
    :cvar UNSUPPORTED_RESPONSE_TYPE: The authorization server does not
        support obtaining an authorization code using this method (RFC
        6749 Section 4.1.2.1).
    :cvar SERVER_ERROR: The authorization server encountered an
        unexpected condition that prevented it from fulfilling the
        request  (RFC 6749 Section 4.1.2.1).
    :cvar TEMPORARILY_UNAVAILABLE: The authorization server is currently
        unable to handle the request due to a temporary overloading or
        maintenance of the server (RFC 6749 Section 4.1.2.1).
    """

    INVALID_REQUEST = "invalid_request"
    INVALID_CLIENT = "invalid_client"
    INVALID_GRANT = "invalid_grant"
    UNAUTHORIZED_CLIENT = "unauthorized_client"
    UNSUPPORTED_GRANT_TYPE = "unsupported_grant_type"
    INVALID_SCOPE = "invalid_scope"
    INVALID_REDIRECT_URI = "invalid_redirect_uri"
    INVALID_CLIENT_METADATA = "invalid_client_metadata"
    INVALID_CLIENT_ID = "invalid_client_id"
    ACCESS_DENIED = "access_denied"
    UNSUPPORTED_RESPONSE_TYPE = "unsupported_response_type"
    SERVER_ERROR = "server_error"
    TEMPORARILY_UNAVAILABLE = "temporarily_unavailable"


class Object(BaseModel):
    """Superclass of all object classes to allow extensions.

    Inheritance from Object provides an inherent extension mechanism
    permitting custom data to be included in a separate namespace.

    :ivar extension: Contains an extension.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    extension: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class PhaseCodeKindValue(Enum):
    """
    :cvar VALUE_225: ABC to Neutral
    :cvar VALUE_224: Involving all phases
    :cvar VALUE_193: AB to Neutral
    :cvar VALUE_41: Phases A, C and neutral.
    :cvar VALUE_97: BC to neutral.
    :cvar VALUE_132: Phases A to B
    :cvar VALUE_96: Phases A and C
    :cvar VALUE_66: Phases B to C
    :cvar VALUE_129: Phases A to neutral.
    :cvar VALUE_65: Phases B to neutral.
    :cvar VALUE_33: Phases C to neutral.
    :cvar VALUE_128: Phase A.
    :cvar VALUE_64: Phase B.
    :cvar VALUE_32: Phase C.
    :cvar VALUE_16: Neutral
    :cvar VALUE_272: Phase S2 to neutral.
    :cvar VALUE_784: Phase S1, S2 to neutral.
    :cvar VALUE_528: Phase S1 to Neutral
    :cvar VALUE_256: Phase S2.
    :cvar VALUE_768: Phase S1 to S2
    :cvar VALUE_769: Phase S1, S2 to N
    :cvar VALUE_0: Not applicable to any phase
    :cvar VALUE_136: Phase A current relative to Phase A voltage
    :cvar VALUE_72: Phase B current or voltage relative to Phase A
        voltage
    :cvar VALUE_40: Phase C current or voltage relative to Phase A
        voltage
    :cvar VALUE_17: Neutral to ground
    :cvar VALUE_512: Phase S1
    """

    VALUE_225 = 225
    VALUE_224 = 224
    VALUE_193 = 193
    VALUE_41 = 41
    VALUE_97 = 97
    VALUE_132 = 132
    VALUE_96 = 96
    VALUE_66 = 66
    VALUE_129 = 129
    VALUE_65 = 65
    VALUE_33 = 33
    VALUE_128 = 128
    VALUE_64 = 64
    VALUE_32 = 32
    VALUE_16 = 16
    VALUE_272 = 272
    VALUE_784 = 784
    VALUE_528 = 528
    VALUE_256 = 256
    VALUE_768 = 768
    VALUE_769 = 769
    VALUE_0 = 0
    VALUE_136 = 136
    VALUE_72 = 72
    VALUE_40 = 40
    VALUE_17 = 17
    VALUE_512 = 512


class QualityOfReadingValue(Enum):
    """
    :cvar VALUE_0: data that has gone through all required validation
        checks and either passed them all or has been verified
    :cvar VALUE_7: Replaced or approved by a human
    :cvar VALUE_8: data value was replaced by a machine computed value
        based on analysis of historical data using the same type of
        measurement.
    :cvar VALUE_9: data value was computed using linear interpolation
        based on the readings before and after it
    :cvar VALUE_10: data that has failed one or more checks
    :cvar VALUE_11: data that has been calculated (using logic or
        mathematical operations)
    :cvar VALUE_12: data that has been calculated as a projection or
        forecast of future readings
    :cvar VALUE_13: indicates that the quality of this reading has mixed
        characteristics
    :cvar VALUE_14: data that has not gone through the validation
    :cvar VALUE_15: the values have been adjusted to account for weather
    :cvar VALUE_16: specifies that a characteristic applies other than
        those defined
    :cvar VALUE_17: data that has been validated and possibly edited
        and/or estimated in accordance with approved procedures
    :cvar VALUE_18: data that failed at least one of the required
        validation checks but was determined to represent actual usage
    :cvar VALUE_19: data that is valid and acceptable for billing
        purposes
    """

    VALUE_0 = 0
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19


class ResponseType(Enum):
    """
    [extension] OAuth 2.0 ESPI supported response types.

    :cvar CODE: Indicates a request for an authorization code (RFC 6749
        Section 4.1.1)
    """

    CODE = "code"


class ServiceKindValue(Enum):
    """
    :cvar VALUE_0: Electricity service.
    :cvar VALUE_1: Gas service.
    :cvar VALUE_2: Water service.
    :cvar VALUE_3: Time service.
    :cvar VALUE_4: Heat service.
    :cvar VALUE_5: Refuse (waster) service.
    :cvar VALUE_6: Sewerage service.
    :cvar VALUE_7: Rates (e.g. tax, charge, toll, duty, tariff, etc.)
        service.
    :cvar VALUE_8: TV license service.
    :cvar VALUE_9: Internet service.
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9


class StatusCodeValue(Enum):
    """
    :cvar VALUE_200: Ok
    :cvar VALUE_201: Created
    :cvar VALUE_202: Accepted
    :cvar VALUE_204: No Content
    :cvar VALUE_301: Moved Permanently
    :cvar VALUE_302: Redirect
    :cvar VALUE_304: Not Modified
    :cvar VALUE_400: Bad Request
    :cvar VALUE_401: Unauthorized
    :cvar VALUE_403: Forbidden
    :cvar VALUE_404: Not Found
    :cvar VALUE_405: Method Not Allowed
    :cvar VALUE_410: Gone
    :cvar VALUE_500: Internal Server Error
    """

    VALUE_200 = 200
    VALUE_201 = 201
    VALUE_202 = 202
    VALUE_204 = 204
    VALUE_301 = 301
    VALUE_302 = 302
    VALUE_304 = 304
    VALUE_400 = 400
    VALUE_401 = 401
    VALUE_403 = 403
    VALUE_404 = 404
    VALUE_405 = 405
    VALUE_410 = 410
    VALUE_500 = 500


class ThirdPartyApplicationTypeValue(Enum):
    """
    :cvar VALUE_1: The application is on the web
    :cvar VALUE_2: The application is on a desktop
    :cvar VALUE_3: The application is on a mobile device
    :cvar VALUE_4: The application is on another device
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class ThirdPartyApplicationUseValue(Enum):
    """
    :cvar VALUE_1: Energy Management
    :cvar VALUE_2: Analytical
    :cvar VALUE_3: Governmental
    :cvar VALUE_4: Academic
    :cvar VALUE_5: Law Enforcement
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class ThirdPartyApplicatonStatusValue(Enum):
    """
    :cvar VALUE_1: Development
    :cvar VALUE_2: Review/Test
    :cvar VALUE_3: Live
    :cvar VALUE_4: Remove
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class TimeAttributeKindValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_1: 10-minute
    :cvar VALUE_2: 15-minute
    :cvar VALUE_3: 1-minute
    :cvar VALUE_4: 24-hour
    :cvar VALUE_5: 30-minute
    :cvar VALUE_6: 5-minute
    :cvar VALUE_7: 60-minute
    :cvar VALUE_10: 2-minute
    :cvar VALUE_14: 3-minute
    :cvar VALUE_15: Within the present period of time
    :cvar VALUE_16: Shifted within the previous monthly cycle and data
        set
    :cvar VALUE_31: 20-minute interval
    :cvar VALUE_50: 60-minute Fixed Block
    :cvar VALUE_51: 30-minute Fixed Block
    :cvar VALUE_52: 20-minute Fixed Block
    :cvar VALUE_53: 15-minute Fixed Block
    :cvar VALUE_54: 10-minute Fixed Block
    :cvar VALUE_55: 5-minute Fixed Block
    :cvar VALUE_56: 1-minute Fixed Block
    :cvar VALUE_57: 60-minute Rolling Block with 30-minute sub-intervals
    :cvar VALUE_58: 60-minute Rolling Block with 20-minute sub-intervals
    :cvar VALUE_59: 60-minute Rolling Block with 15-minute sub-intervals
    :cvar VALUE_60: 60-minute Rolling Block with 12-minute sub-intervals
    :cvar VALUE_61: 60-minute Rolling Block with 10-minute sub-intervals
    :cvar VALUE_62: 60-minute Rolling Block with 6-minute sub-intervals
    :cvar VALUE_63: 60-minute Rolling Block with 5-minute sub-intervals
    :cvar VALUE_64: 60-minute Rolling Block with 4-minute sub-intervals
    :cvar VALUE_65: 30-minute Rolling Block with 15-minute sub-intervals
    :cvar VALUE_66: 30-minute Rolling Block with 10-minute sub-intervals
    :cvar VALUE_67: 30-minute Rolling Block with 6-minute sub-intervals
    :cvar VALUE_68: 30-minute Rolling Block with 5-minute sub-intervals
    :cvar VALUE_69: 30-minute Rolling Block with 3-minute sub-intervals
    :cvar VALUE_70: 30-minute Rolling Block with 2-minute sub-intervals
    :cvar VALUE_71: 15-minute Rolling Block with 5-minute sub-intervals
    :cvar VALUE_72: 15-minute Rolling Block with 3-minute sub-intervals
    :cvar VALUE_73: 15-minute Rolling Block with 1-minute sub-intervals
    :cvar VALUE_74: 10-minute Rolling Block with 5-minute sub-intervals
    :cvar VALUE_75: 10-minute Rolling Block with 2-minute sub-intervals
    :cvar VALUE_76: 10-minute Rolling Block with 1-minute sub-intervals
    :cvar VALUE_77: 5-minute Rolling Block with 1-minute sub-intervals
    """

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_10 = 10
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_31 = 31
    VALUE_50 = 50
    VALUE_51 = 51
    VALUE_52 = 52
    VALUE_53 = 53
    VALUE_54 = 54
    VALUE_55 = 55
    VALUE_56 = 56
    VALUE_57 = 57
    VALUE_58 = 58
    VALUE_59 = 59
    VALUE_60 = 60
    VALUE_61 = 61
    VALUE_62 = 62
    VALUE_63 = 63
    VALUE_64 = 64
    VALUE_65 = 65
    VALUE_66 = 66
    VALUE_67 = 67
    VALUE_68 = 68
    VALUE_69 = 69
    VALUE_70 = 70
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73
    VALUE_74 = 74
    VALUE_75 = 75
    VALUE_76 = 76
    VALUE_77 = 77


class TimePeriodOfInterestValue(Enum):
    """
    :cvar VALUE_0: Not Applicable
    :cvar VALUE_8: Captured during the billing period starting at
        midnight of the first day of the billing period (as defined by
        the billing cycle day). If during the current billing period, it
        specifies a period from the start of the current billing period
        until "now".
    :cvar VALUE_11: Daily Period starting at midnight. If for the
        current day, this specifies the time from midnight to "now".
    :cvar VALUE_13: Monthly period starting at midnight on the first day
        of the month. If within the current month, this specifies the
        period from the start of the month until "now."
    :cvar VALUE_22: A season of time spanning multiple months. E.g.
        "Summer," "Spring," "Fall," and "Winter" based cycle. If within
        the current season, it specifies the period from the start of
        the current season until "now."
    :cvar VALUE_24: Weekly period starting at midnight on the first day
        of the week and ending the instant before midnight the last day
        of the week. If within the current week, it specifies the period
        from the start of the week until "now."
    :cvar VALUE_32: For the period defined by the start and end of the
        TimePeriod element in the message.
    """

    VALUE_0 = 0
    VALUE_8 = 8
    VALUE_11 = 11
    VALUE_13 = 13
    VALUE_22 = 22
    VALUE_24 = 24
    VALUE_32 = 32


class TokenEndPointMethod(Enum):
    """
    [extension] Token endpoint method in OAuth 2.0.

    :cvar CLIENT_SECRET_BASIC: [extension] Indicates the client uses
        HTTP Basic authentication (RFC 6749 Section 2.3.1).
    """

    CLIENT_SECRET_BASIC = "client_secret_basic"


class TokenType(Enum):
    """
    [extension] OAuth 2.0 ESPI supported token types.

    :cvar BEARER: A security token with the property that any party in
        possession of the token (a "bearer") can use the token in any
        way that any other party in possession of it can.  Using a
        bearer token does not require a bearer to prove possession of
        cryptographic key material (proof-of-possession) (RFC6750
        Section 1.2).
    """

    BEARER = "Bearer"


class UnitMultiplierKindValue(Enum):
    """
    :cvar VALUE_MINUS_12: Pico 10**-12
    :cvar VALUE_MINUS_9: Nano 10**-9
    :cvar VALUE_MINUS_6: Micro 10**-6
    :cvar VALUE_MINUS_3: Milli 10**-3
    :cvar VALUE_MINUS_2: Centi 10**-2
    :cvar VALUE_MINUS_1: Deci 10**-1
    :cvar VALUE_3_1: Kilo 10**3
    :cvar VALUE_6_1: Mega 10**6
    :cvar VALUE_9_1: Giga 10**9
    :cvar VALUE_12_1: Tera 10**12
    :cvar VALUE_0: Not Applicable or "x1"
    :cvar VALUE_1_1: deca 10**1
    :cvar VALUE_2_1: hecto 10**2
    """

    VALUE_MINUS_12 = -12
    VALUE_MINUS_9 = -9
    VALUE_MINUS_6 = -6
    VALUE_MINUS_3 = -3
    VALUE_MINUS_2 = -2
    VALUE_MINUS_1 = -1
    VALUE_3_1 = 3
    VALUE_6_1 = 6
    VALUE_9_1 = 9
    VALUE_12_1 = 12
    VALUE_0 = 0
    VALUE_1_1 = 1
    VALUE_2_1 = 2


class UnitSymbolKindValue(Enum):
    """
    :cvar VALUE_61: Apparent power, Volt Ampere (See also real power and
        reactive power.), VA
    :cvar VALUE_38: Real power, Watt. By definition, one Watt equals one
        Joule per second. Electrical power may have real and reactive
        components. The real portion of electrical power (I²R) or
        VIcos?, is expressed in Watts. (See also apparent power and
        reactive power.), W
    :cvar VALUE_63: Reactive power, Volt Ampere reactive. The “reactive”
        or “imaginary” component of electrical power (VISin?). (See also
        real power and apparent power)., VAr
    :cvar VALUE_71: Apparent energy, Volt Ampere hours, VAh
    :cvar VALUE_72: Real energy, Watt hours, Wh
    :cvar VALUE_73: Reactive energy, Volt Ampere reactive hours, VArh
    :cvar VALUE_29: Electric potential, Volt (W/A), V
    :cvar VALUE_30: Electric resistance, Ohm (V/A), O
    :cvar VALUE_5: Current, ampere, A
    :cvar VALUE_25: Electric capacitance, Farad (C/V), °C
    :cvar VALUE_28: Electric inductance, Henry (Wb/A), H
    :cvar VALUE_23: Relative temperature in degrees Celsius. In the SI
        unit system the symbol is ºC. Electric charge is measured in
        coulomb that has the unit symbol C. To distinguish degree
        Celsius from coulomb the symbol used in the UML is degC. Reason
        for not using ºC is the special character º is difficult to
        manage in software.
    :cvar VALUE_27: Time, seconds, s
    :cvar VALUE_159: Time, minute = s * 60, min
    :cvar VALUE_160: Time, hour = minute * 60, h
    :cvar VALUE_9: Plane angle, degrees, deg
    :cvar VALUE_10: Plane angle, Radian (m/m), rad
    :cvar VALUE_31: Energy joule, (N·m = C·V = W·s), J
    :cvar VALUE_32: Force newton, (kg m/s²), N
    :cvar VALUE_53: Electric conductance, Siemens (A / V = 1 / O), S
    :cvar VALUE_0: N/A, None
    :cvar VALUE_33: Frequency hertz, (1/s), Hz
    :cvar VALUE_3: Mass in gram, g
    :cvar VALUE_39: Pressure, Pascal (N/m²)(Note: the absolute or
        relative measurement of pressure is implied with this entry. See
        below for more explicit forms.), Pa
    :cvar VALUE_2: Length, meter, m
    :cvar VALUE_41: Area, square meter, m²
    :cvar VALUE_42: Volume, cubic meter, m³
    :cvar VALUE_69: Amps squared, amp squared, A2
    :cvar VALUE_105: ampere-squared, Ampere-squared hour, A²h
    :cvar VALUE_70: Amps squared time, square amp second, A²s
    :cvar VALUE_106: Ampere-hours, Ampere-hours, Ah
    :cvar VALUE_152: Current, Ratio of Amperages, A/A
    :cvar VALUE_103: A/m, magnetic field strength, Ampere per metre, A/m
    :cvar VALUE_68: Amp seconds, amp seconds, As
    :cvar VALUE_79: Sound pressure level, Bel, acoustic, Combine with
        multiplier prefix “d” to form decibels of Sound Pressure
        Level“dB (SPL).”, B (SPL)
    :cvar VALUE_113: Signal Strength, Bel-mW, normalized to 1mW. Note:
        to form “dBm” combine “Bm” with multiplier “d”. Bm
    :cvar VALUE_22: Radioactivity, Becquerel (1/s), Bq
    :cvar VALUE_132: Energy, British Thermal Units, BTU
    :cvar VALUE_133: Power, BTU per hour, BTU/h
    :cvar VALUE_8: Luminous intensity, candela, cd
    :cvar VALUE_76: Number of characters, characters, char
    :cvar VALUE_75: Rate of change of frequency, hertz per second, Hz/s
    :cvar VALUE_114: Application Value, encoded value, code
    :cvar VALUE_65: Power factor, Dimensionless, cos?
    :cvar VALUE_111: Amount of substance, counter value, count
    :cvar VALUE_119: Volume, cubic feet, ft³
    :cvar VALUE_120: Volume, cubic feet, ft³(compensated)
    :cvar VALUE_123: Volumetric flow rate, compensated cubic feet per
        hour, ft³(compensated)/h
    :cvar VALUE_78: Turbine inertia, gram·meter2 (Combine with
        multiplier prefix “k” to form kg·m2.), gm²
    :cvar VALUE_144: Concentration, The ratio of the mass of a solute
        divided by the mass of the solution., g/g
    :cvar VALUE_21: Absorbed dose, Gray (J/kg), GY
    :cvar VALUE_150: Frequency, Rate of frequency change, Hz/Hz
    :cvar VALUE_77: Data rate, characters per second, char/s
    :cvar VALUE_130: Volume, imperial gallons, ImperialGal
    :cvar VALUE_131: Volumetric flow rate, Imperial gallons per hour,
        ImperialGal/h
    :cvar VALUE_51: Heat capacity, Joule/Kelvin, J/K
    :cvar VALUE_165: Specific energy, Joules / kg, J/kg
    :cvar VALUE_6: Temperature, Kelvin, K
    :cvar VALUE_158: Catalytic activity, katal = mol / s, kat
    :cvar VALUE_47: Moment of mass ,kilogram meter (kg·m), M
    :cvar VALUE_48: Density, gram/cubic meter (combine with prefix
        multiplier “k” to form kg/ m³), g/m³
    :cvar VALUE_134: Volume, litre = dm3 = m3/1000., L
    :cvar VALUE_157: Volume, litre, with the value compensated for
        weather effects, L(compensated)
    :cvar VALUE_138: Volumetric flow rate, litres (compensated) per
        hour, L(compensated)/h
    :cvar VALUE_137: Volumetric flow rate, litres per hour, L/h
    :cvar VALUE_143: Concentration, The ratio of the volume of a solute
        divided by the volume of the solution., L/L
    :cvar VALUE_82: Volumetric flow rate, Volumetric flow rate, L/s
    :cvar VALUE_156: Volume, litre, with the value uncompensated for
        weather effects., L(uncompensated)
    :cvar VALUE_139: Volumetric flow rate, litres (uncompensated) per
        hour, L(uncompensated)/h
    :cvar VALUE_35: Luminous flux, lumen (cd sr), Lm
    :cvar VALUE_34: Illuminance lux, (lm/m²), L(uncompensated)/h
    :cvar VALUE_49: Viscosity, meter squared / second, m²/s
    :cvar VALUE_167: Volume, cubic meter, with the value compensated for
        weather effects., m3(compensated)
    :cvar VALUE_126: Volumetric flow rate, compensated cubic meters per
        hour, ³(compensated)/h
    :cvar VALUE_125: Volumetric flow rate, cubic meters per hour, m³/h
    :cvar VALUE_45: m3PerSec, cubic meters per second, m³/s
    :cvar VALUE_166: m3uncompensated, cubic meter, with the value
        uncompensated for weather effects., m3(uncompensated)
    :cvar VALUE_127: Volumetric flow rate, uncompensated cubic meters
        per hour, m³(uncompensated)/h
    :cvar VALUE_118: EndDeviceEvent, value to be interpreted as a
        EndDeviceEventCode, meCode
    :cvar VALUE_7: Amount of substance, mole, mol
    :cvar VALUE_147: Concentration, Molality, the amount of solute in
        moles and the amount of solvent in kilograms., mol/kg
    :cvar VALUE_145: Concentration, The amount of substance
        concentration, (c), the amount of solvent in moles divided by
        the volume of solution in m³., mol/ m³
    :cvar VALUE_146: Concentration, Molar fraction (?), the ratio of the
        molar amount of a solute divided by the molar amount of the
        solution.,mol/mol
    :cvar VALUE_80: Monetary unit, Generic money (Note: Specific
        monetary units are identified the currency class)., ¤
    :cvar VALUE_148: Length, Ratio of length, m/m
    :cvar VALUE_46: Fuel efficiency, meters / cubic meter, m/m³
    :cvar VALUE_43: Velocity, meters per second (m/s), m/s
    :cvar VALUE_44: Acceleration, meters per second squared, m/s²
    :cvar VALUE_102: resistivity, ? (rho), ?m
    :cvar VALUE_155: Pressure, Pascal, absolute pressure, PaA
    :cvar VALUE_140: Pressure, Pascal, gauge pressure, PaG
    :cvar VALUE_141: Pressure, Pounds per square inch, absolute, psiA
    :cvar VALUE_142: Pressure, Pounds per square inch, gauge, psiG
    :cvar VALUE_100: Quantity power, Q, Q
    :cvar VALUE_161: Quantity power, Q measured at 45º, Q45
    :cvar VALUE_163: Quantity energy, Q measured at 45º, Q45h
    :cvar VALUE_162: Quantity power, Q measured at 60º, Q60
    :cvar VALUE_164: Quantity energy, Qh measured at 60º, Q60h
    :cvar VALUE_101: Quantity energy, Qh, Qh
    :cvar VALUE_54: Angular velocity, radians per second, rad/s
    :cvar VALUE_154: Amount of rotation, Revolutions, rev
    :cvar VALUE_4: Rotational speed, Rotations per second, rev/s
    :cvar VALUE_149: Time, Ratio of time (can be combined with an
        multiplier prefix to show rates such as a clock drift rate, e.g.
        “µs/s”), s/s
    :cvar VALUE_11: Solid angle, Steradian (m2/m2), sr
    :cvar VALUE_109: State, "1" = "true", "live", "on", "high", "set";
        "0" = "false", "dead", "off", "low", "cleared". Note: A Boolean
        value is preferred but other values may be supported, status
    :cvar VALUE_24: Doe equivalent, Sievert (J/kg), Sv
    :cvar VALUE_37: Magnetic flux density, Tesla (Wb/m2), T
    :cvar VALUE_169: Energy, Therm, therm
    :cvar VALUE_108: Timestamp, time and date per ISO 8601 format,
        timeStamp
    :cvar VALUE_128: Volume, US gallons, Gal
    :cvar VALUE_129: Volumetric flow rate, US gallons per hour, USGal/h
    :cvar VALUE_67: Volts squared, Volt squared (W2/A2), V²
    :cvar VALUE_104: volt-squared hour, Volt-squared-hours, V²h
    :cvar VALUE_117: Kh-Vah, apparent energy metering constant, VAh/rev
    :cvar VALUE_116: Kh-VArh, reactive energy metering constant,
        VArh/rev
    :cvar VALUE_74: Magnetic flux, Volts per Hertz, V/Hz
    :cvar VALUE_151: Voltage, Ratio of voltages (e.g. mV/V), V/V
    :cvar VALUE_66: Volt seconds, Volt seconds (Ws/A), Vs
    :cvar VALUE_36: Magnetic flux, Weber (V s), Wb
    :cvar VALUE_107: Wh/m3, energy per volume, Wh/m³
    :cvar VALUE_115: Kh-Wh, active energy metering constant, Wh/rev
    :cvar VALUE_50: Thermal conductivity, Watt/meter Kelvin, W/m K
    :cvar VALUE_81: Ramp rate, Watts per second, W/s
    :cvar VALUE_153: Power Factor, PF, W/VA
    :cvar VALUE_168: Signal Strength, Ratio of power, W/W
    """

    VALUE_61 = 61
    VALUE_38 = 38
    VALUE_63 = 63
    VALUE_71 = 71
    VALUE_72 = 72
    VALUE_73 = 73
    VALUE_29 = 29
    VALUE_30 = 30
    VALUE_5 = 5
    VALUE_25 = 25
    VALUE_28 = 28
    VALUE_23 = 23
    VALUE_27 = 27
    VALUE_159 = 159
    VALUE_160 = 160
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_31 = 31
    VALUE_32 = 32
    VALUE_53 = 53
    VALUE_0 = 0
    VALUE_33 = 33
    VALUE_3 = 3
    VALUE_39 = 39
    VALUE_2 = 2
    VALUE_41 = 41
    VALUE_42 = 42
    VALUE_69 = 69
    VALUE_105 = 105
    VALUE_70 = 70
    VALUE_106 = 106
    VALUE_152 = 152
    VALUE_103 = 103
    VALUE_68 = 68
    VALUE_79 = 79
    VALUE_113 = 113
    VALUE_22 = 22
    VALUE_132 = 132
    VALUE_133 = 133
    VALUE_8 = 8
    VALUE_76 = 76
    VALUE_75 = 75
    VALUE_114 = 114
    VALUE_65 = 65
    VALUE_111 = 111
    VALUE_119 = 119
    VALUE_120 = 120
    VALUE_123 = 123
    VALUE_78 = 78
    VALUE_144 = 144
    VALUE_21 = 21
    VALUE_150 = 150
    VALUE_77 = 77
    VALUE_130 = 130
    VALUE_131 = 131
    VALUE_51 = 51
    VALUE_165 = 165
    VALUE_6 = 6
    VALUE_158 = 158
    VALUE_47 = 47
    VALUE_48 = 48
    VALUE_134 = 134
    VALUE_157 = 157
    VALUE_138 = 138
    VALUE_137 = 137
    VALUE_143 = 143
    VALUE_82 = 82
    VALUE_156 = 156
    VALUE_139 = 139
    VALUE_35 = 35
    VALUE_34 = 34
    VALUE_49 = 49
    VALUE_167 = 167
    VALUE_126 = 126
    VALUE_125 = 125
    VALUE_45 = 45
    VALUE_166 = 166
    VALUE_127 = 127
    VALUE_118 = 118
    VALUE_7 = 7
    VALUE_147 = 147
    VALUE_145 = 145
    VALUE_146 = 146
    VALUE_80 = 80
    VALUE_148 = 148
    VALUE_46 = 46
    VALUE_43 = 43
    VALUE_44 = 44
    VALUE_102 = 102
    VALUE_155 = 155
    VALUE_140 = 140
    VALUE_141 = 141
    VALUE_142 = 142
    VALUE_100 = 100
    VALUE_161 = 161
    VALUE_163 = 163
    VALUE_162 = 162
    VALUE_164 = 164
    VALUE_101 = 101
    VALUE_54 = 54
    VALUE_154 = 154
    VALUE_4 = 4
    VALUE_149 = 149
    VALUE_11 = 11
    VALUE_109 = 109
    VALUE_24 = 24
    VALUE_37 = 37
    VALUE_169 = 169
    VALUE_108 = 108
    VALUE_128 = 128
    VALUE_129 = 129
    VALUE_67 = 67
    VALUE_104 = 104
    VALUE_117 = 117
    VALUE_116 = 116
    VALUE_74 = 74
    VALUE_151 = 151
    VALUE_66 = 66
    VALUE_36 = 36
    VALUE_107 = 107
    VALUE_115 = 115
    VALUE_50 = 50
    VALUE_81 = 81
    VALUE_153 = 153
    VALUE_168 = 168


class UsagePointConnectedKind(Enum):
    """
    State of the usage point with respect to connection to the network.

    :cvar CONNECTED: The usage point is connected to the network and
        able to receive or send the applicable commodity (electricity,
        gas, water, etc.).
    :cvar LOGICALLY_DISCONNECTED: The usage point has been disconnected
        through operation of a disconnect function within the meter
        present at the usage point.  The usage point is unable to
        receive or send the applicable commodity (electricity, gas,
        water, etc.)  A logical disconnect can often be achieved without
        utilising a field crew.
    :cvar PHYSICALLY_DISCONNECTED: The usage point has been disconnected
        from the network at a point upstream of the meter. The usage
        point is unable to receive or send the applicable commodity
        (electricity, gas, water, etc.). A physical disconnect is often
        achieved by utilising a field crew.
    """

    CONNECTED = "connected"
    LOGICALLY_DISCONNECTED = "logicallyDisconnected"
    PHYSICALLY_DISCONNECTED = "physicallyDisconnected"


class TOuorCpporConsumptionTier(Enum):
    """
    [extension] Type of billing tariff profile uses.

    :cvar TOU: Time of Use
    :cvar CPP: Consumption Peak Period
    :cvar CONSUMPTIONTIER: Consumption Tier
    """

    TOU = "tou"
    CPP = "cpp"
    CONSUMPTIONTIER = "consumptiontier"


class BatchItemInfo(Object):
    """
    Includes elements that make it possible to include multiple transactions in a
    single (batch) request.

    :ivar name: An identifier for this object that is only unique within
        the containing collection.
    :ivar operation: Specifies the operation requested of this item.
    :ivar status_code: Indicates the status code of the associated
        transaction.
    :ivar status_reason: Indicates the reason for the indicated status
        code.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    name: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 2,
            "format": "base16",
        },
    )
    operation: Optional[Union[int, CrudoperationValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    status_code: Optional[Union[int, StatusCodeValue]] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
        },
    )
    status_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "statusReason",
            "type": "Element",
            "max_length": 256,
        },
    )


class BatchList(BatchListType):
    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)


class BillingChargeSource(Object):
    """
    [extension] Information about source of billing charge.

    :ivar agency_name: [extension] Name of billing source
    """

    model_config = ConfigDict(defer_build=True)
    agency_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "agencyName",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        },
    )


class DateTimeInterval(Object):
    """Interval of date and time.

    End is not included because it can be derived from the start and the
    duration.

    :ivar duration: [correction] Duration of the interval, in seconds.
    :ivar start: [correction] Date and time that this interval started.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    duration: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    start: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class PnodeRef(Object):
    """
    [extension] Reference to a Pnode.

    :ivar apnode_type: type of pnode.
    :ivar ref: Reference to a Pnode.
    :ivar start_effective_date: [extension] Starting Effective Date of
        Pnode assignment
    :ivar end_effective_date: [extension] Ending Effective Date of Pnode
        assignment
    """

    model_config = ConfigDict(defer_build=True)
    apnode_type: ApnodeType = field(
        metadata={
            "name": "apnodeType",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    ref: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 256,
        }
    )
    start_effective_date: Optional[int] = field(
        default=None,
        metadata={
            "name": "startEffectiveDate",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )
    end_effective_date: Optional[int] = field(
        default=None,
        metadata={
            "name": "endEffectiveDate",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )


class RationalNumber(Object):
    """
    [extension] Rational number = 'numerator' / 'denominator'.
    """

    model_config = ConfigDict(defer_build=True)
    numerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )
    denominator: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )


class ReadingInterharmonic(Object):
    """
    [extension] Interharmonics are represented as a rational number 'numerator' /
    'denominator', and harmonics are represented using the same mechanism and
    identified by 'denominator'=1.
    """

    model_config = ConfigDict(defer_build=True)
    numerator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )
    denominator: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )


class ReadingQuality(Object):
    """Quality of a specific reading value or interval reading value.

    Note that more than one Quality may be applicable to a given
    Reading. Typically not used unless problems or unusual conditions
    occur (i.e., quality for each Reading is assumed to be 'Good'
    (valid) unless stated otherwise in associated ReadingQuality).

    :ivar quality: Quality, to be specified if different than
        ReadingType.defaultQuality. The specific format is specified per
        the standard is defined in QualityOfReading.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    quality: Union[int, QualityOfReadingValue] = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class ServiceCategory(Object):
    """
    Category of service provided to the customer.

    :ivar kind: Service classification Examples are: 0 - electricity 1 -
        gas The list of specific valid values per the standard are
        itemized in ServiceKind.
    """

    model_config = ConfigDict(defer_build=True)
    kind: Union[int, ServiceKindValue] = field(
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )


class ServiceStatus(Object):
    """
    Contains the current status of the service.

    :ivar current_status: The current status of the service.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    current_status: Union[int, EspiserviceStatusValue] = field(
        metadata={
            "name": "currentStatus",
            "type": "Element",
            "required": True,
        }
    )


class SummaryMeasurement(Object):
    """
    An aggregated summary measurement reading.

    :ivar power_of_ten_multiplier: The multiplier part of the unit of
        measure, e.g. “kilo” (k)
    :ivar time_stamp: The date and time (if needed) of the summary
        measurement.
    :ivar uom: The units of the reading, e.g. “Wh”
    :ivar value: The value of the summary measurement.
    :ivar reading_type_ref: [extension] Reference to a full ReadingType.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    power_of_ten_multiplier: Optional[Union[int, UnitMultiplierKindValue]] = (
        field(
            default=None,
            metadata={
                "name": "powerOfTenMultiplier",
                "type": "Element",
            },
        )
    )
    time_stamp: Optional[int] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Element",
        },
    )
    uom: Optional[Union[int, UnitSymbolKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    reading_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "readingTypeRef",
            "type": "Element",
        },
    )


class TariffRiderRef(Object):
    """
    [extension] Reference to a Tariff Rider.

    :ivar rider_type: [extension] Rate options applied to the base
        tariff profile
    :ivar enrollment_status: [extension] Retail Customer's Tariff Rider
        enrollment status
    :ivar effective_date: [extension] Effective date of Retail
        Customer's Tariff Rider enrollment status
    """

    model_config = ConfigDict(defer_build=True)
    rider_type: str = field(
        metadata={
            "name": "riderType",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 256,
        }
    )
    enrollment_status: EnrollmentStatus = field(
        metadata={
            "name": "enrollmentStatus",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    effective_date: int = field(
        metadata={
            "name": "effectiveDate",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )


class AggregateNodeRef(Object):
    """
    [extension] Reference to an AggregateNode (could be a load aggregation point
    which is a specialization of AggregateNode).

    :ivar anode_type: Type of aggregateNode.
    :ivar ref: Reference to an AggregateNode.
    :ivar start_effective_date: [extension] Starting Effective Date of
        ANode assignment
    :ivar end_effective_date: [extension] Ending Effective Date of ANode
        assignment
    :ivar pnode_ref:
    """

    model_config = ConfigDict(defer_build=True)
    anode_type: AnodeType = field(
        metadata={
            "name": "anodeType",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    ref: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 256,
        }
    )
    start_effective_date: Optional[int] = field(
        default=None,
        metadata={
            "name": "startEffectiveDate",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )
    end_effective_date: Optional[int] = field(
        default=None,
        metadata={
            "name": "endEffectiveDate",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )
    pnode_ref: List[PnodeRef] = field(
        default_factory=list,
        metadata={
            "name": "pnodeRef",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )


class IdentifiedObject(Object):
    """
    This is a root class to provide common naming attributes for all classes
    needing naming attributes.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    batch_item_info: Optional[BatchItemInfo] = field(
        default=None,
        metadata={
            "name": "batchItemInfo",
            "type": "Element",
        },
    )


class IntervalReading(Object):
    """Specific value measured by a meter or other asset.

    Each Reading is associated with a specific ReadingType.

    :ivar cost: [correction] Specifies a cost associated with this
        reading, in hundred-thousandths of the currency specified in the
        ReadingType for this reading. (e.g., 840 = USD, US dollar)
    :ivar reading_quality: One or more quality of reading values for the
        current interval reading.
    :ivar time_period: The date time and duration of a reading. If not
        specified, readings for each “intervalLength” in ReadingType are
        present.
    :ivar value: [correction] Value in units specified by ReadingType
    :ivar consumption_tier: [extension] Code for consumption tier
        associated with reading.
    :ivar tou: [extension] Code for the TOU type of reading.
    :ivar cpp: [extension] Critical peak period (CPP) bucket the reading
        value is attributed to. Value 0 means not applicable. Even
        though CPP is usually considered a specialized form of time of
        use 'tou', this attribute is defined explicitly for flexibility.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    cost: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    reading_quality: List[ReadingQuality] = field(
        default_factory=list,
        metadata={
            "name": "ReadingQuality",
            "type": "Element",
        },
    )
    time_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "timePeriod",
            "type": "Element",
        },
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    consumption_tier: Optional[int] = field(
        default=None,
        metadata={
            "name": "consumptionTier",
            "type": "Element",
        },
    )
    tou: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cpp: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class LineItem(Object):
    """
    [extension] Line item of detail for additional cost.

    :ivar amount: Cost of line item.
    :ivar rounding: Rounded to nearest increment.
    :ivar date_time: Significant date for line item.
    :ivar note: Comment or description of line item.
    :ivar measurement: [extension] relevant measurment for line item.
    :ivar item_kind: [extension] Classification of a line item -- i.e.
        usage charge, taxes, etc...
    :ivar unit_cost: [extension] Per Unit cost.
    :ivar item_period: [extension] Time period covered by the LineItem,
        to support pricing changes in the middle of a billing period
    """

    model_config = ConfigDict(defer_build=True)
    amount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    rounding: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    date_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )
    note: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 256,
        }
    )
    measurement: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )
    item_kind: Union[int, ItemKindValue] = field(
        metadata={
            "name": "itemKind",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    unit_cost: Optional[int] = field(
        default=None,
        metadata={
            "name": "unitCost",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    item_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "itemPeriod",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )


class PnodeRefs(Object):
    """
    [extension] Sequence of references to Pnodes assoicated with a UsagePoint.

    :ivar pnode_ref: pnodeRef structure.
    """

    model_config = ConfigDict(defer_build=True)
    pnode_ref: List[PnodeRef] = field(
        default_factory=list,
        metadata={
            "name": "pnodeRef",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "min_occurs": 1,
        },
    )


class TariffRiderRefs(Object):
    """
    [extension] References to associated Tariff Riders.

    :ivar tariff_rider_ref: [extension] Tariff Rider structure.
    """

    model_config = ConfigDict(defer_build=True)
    tariff_rider_ref: List[TariffRiderRef] = field(
        default_factory=list,
        metadata={
            "name": "tariffRiderRef",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "min_occurs": 1,
        },
    )


class AggregateNodeRefs(Object):
    """
    [extension] References to associated AggregateNodes.
    """

    model_config = ConfigDict(defer_build=True)
    aggregate_node_ref: List[AggregateNodeRef] = field(
        default_factory=list,
        metadata={
            "name": "aggregateNodeRef",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "min_occurs": 1,
        },
    )


class ApplicationInformation(IdentifiedObject):
    """Contains information about a Third Party Application requesting access to
    the DataCustodian services.

    Information requested may include items such as Organization Name, Website, Contact Info, Application Name, Description, Icon, Type, default Notification and Callback endpoints, and may also include agreement with terms of service.
    Atom Links:
    self link to this resource

    :ivar data_custodian_id: [extension] Contains the identifier for the
        Data Custodian. (e.g. "Sandbox Data Custodian")
    :ivar data_custodian_application_status: A code indicating the
        current status of the application. This value is provided by
        Data Custodian, cannot be modified by Third Party. (e.g. "2"
        =&gt; production)
    :ivar third_party_application_description: A description of the
        application. (e.g. "Third Party Application Description is added
        as provided by each TP")
    :ivar third_party_application_status: A code indicating the current
        status of the application. (e.g. "1" =&gt; Development
    :ivar third_party_application_type: A code indicating the type of
        the application. (e.g. "1" =&gt; Web)
    :ivar third_party_application_use: A code indicating the expected
        use of the application. (e.g. "1" =&gt; EnergyManagement)
    :ivar third_party_phone: The phone number of the organization to
        which access will be granted. (For debugging - not to be shared
        with customers). (e.g. "+1 800 673-6377")
    :ivar authorization_server_uri: [extension] Contains the base URI
        link to the authorization server. (e.g.
        "https://server.example.com/DataCustodian")
    :ivar third_party_notify_uri: [extension] URI used to notify
        ThirdParty that subscribed information is available. (e.g.
        "https://server.example.com/ThirdParty/espi/1_1/Notification")
    :ivar authorization_server_authorization_endpoint: [extension] An
        OAuth 2.0 URI used by the client to obtain authorization from
        the resource owner via user-agent redirection -
        {AuthorizationServer}{AuthorizationPath}. (e.g.
        "https://server.example.com/DataCustodian/oauth/authorize"
    :ivar authorization_server_registration_endpoint: [extension] A URI
        used by the client to register a Third Party with a Data
        Custodian via its
        {AuthorizationServer}{AuthorizationServer}{RegistrationPath}.
        (e.g.
        "https://server.example.com/DataCustodian/espi/1_1/register")
    :ivar authorization_server_token_endpoint: [extension] An OAuth 2.0
        URL used by the client to exchange an authorization grant for an
        access token, typically with client authentication. (e.g.
        "https://server.example.com/DataCustodian/oauth/token")
    :ivar data_custodian_bulk_request_uri: [extension]
        {DataCustodianBulkRequestURI}  URI of DataCustodian’s Bulk
        Request endpoint.  The value is provided by the Data Custodian
        and cannot be modified by the ThirdParty. (e.g.
        "https://server.example.com/DataCustodian/espi/1_1/resource/Batch/Bulk/{BulkID}"
        =&gt; bulkID from BR={bulkId} from Scope)
    :ivar data_custodian_resource_endpoint: [extension]
        {ResourceServer}{ResourcePath}. (e.g.
        "https://server.example.com/DataCustodian/espi/1_1/resource")
    :ivar third_party_scope_selection_screen_uri:
        [DEPRECATED][extension] URI of the Scope Selection Screen used
        by the Retail Customer to select the characteristics of the
        Green Button data to be shared with the ThirdParty.  (e.g.
        "https://server.example.com/ThirdParty/espi/1_1/RetailCustomer/ScopeSelection")
    :ivar third_party_user_portal_screen_uri: [extension] URI of a Third
        Party’s web page for use with Green Button Connect My Data (e.g.
        "https://server.example.com/ThirdParty/espi/1_1/home")
    :ivar client_secret: [extension] A secret to be associated with this
        application, used to sign OAuth requests. This value is provided
        by Data Custodian (OAuth client_secret). (e.g. "secret")
    :ivar logo_uri: [extension] The link to the logo image for the
        application. Size greater than 180 x 150 may be cropped or
        reduced (OAuth logo_uri). (e.g.
        "http://server.example.com/ThirdParty/favicon.png")
    :ivar client_name: [extension] The name of the application to which
        access will be granted (OAuth client_name). (e.g. "Green Button
        ThirdParty")
    :ivar client_uri: [extension] The link to the main page of the
        application (OAuth client_uri). (e.g.
        "https://server.example.com/ThirdParty")
    :ivar redirect_uri: [extension] The default redirect back to the
        application after authorization grant (OAuth redirect uri).
        (e.g.
        "https://server.example.com/ThirdParty/espi/1_1/OAuthCallBack")
    :ivar client_id: Contains the identifier for the Third Party (OAuth
        client_id). (e.g. "ThirdParty Name")
    :ivar tos_uri: [extension] A URI that points to a human-readable
        Terms of Service document for the Third Party Application.  The
        Terms of Service usually describes a contractual relationship
        between the Retail Customer and the Third Party Application that
        the Retail Customer accepts when authorizing access to the Third
        Party Application. (e.g.
        "http://server.example.com/ThirdParty/TermsOfService")
    :ivar policy_uri: [extension] A URI that points to a human-readable
        Policy document for the Third Party Application.  The policy
        usually describes how a Retail Customer's energy usage
        information will be used by the Third Party Application. (e.g.
        "http://server.example.com/ThirdParty/UsagePolicy")
    :ivar software_id: [extension] An identifier for the software that
        comprises the Third Party Application.  The software_id is
        asserted by the Third Party software and is intended to be
        shared between all copies of the Third Party software.  The
        value of this field MAY be a UUID [RFC4122]. (e.g.
        "MyCoolGreenButtonAnalyzer")
    :ivar software_version: [extension] A version identifier for the
        software that comprises a Third Party Application.  The value of
        this field is a string that is intended to be compared using
        string equality matching.  The value of the software_version
        SHOULD change on any update to the Third Party software. (e.g.
        "Version 1.00.00")
    :ivar client_id_issued_at: [extension] Time date stamp at which this
        client_id was issued. Note the schema data type is TimeType and
        the presentation in OAuth message flow is xs:dateTime and
        requires a conversion when accessed. (e.g. "1403190000" =&gt;
        2014-06-19T15:00:00Z)
    :ivar client_secret_expires_at: [extension] Date time at which this
        client_secret expires -- value of 0 means the client_secret
        never expires. (e.g. "0" =&gt; never expires)
    :ivar contacts: [extension] Array of email addresses for people
        responsible for the Authorized Third Party Application.  These
        MAY be made available to Retail Customers for support requests
        for the Authorized Third Party application.  The Data Custodian
        Authorization Server MAY use the email addresses as identifiers
        for an Authorized Third Party application administrative page.
        (e.g. "support@energyos.org")
    :ivar token_endpoint_auth_method: [extension] The authentication
        method used by the OAuth 2.0 Token Endpoint to authenticate the
        Third Party Application. (e.g. "client_secret_basic")
    :ivar scope: [extension] Space separated list of scope values the
        Third Party Application may use when requesting access Tokens.
        (e.g.
        "FB=1_3_4_5_8_13_18_19_31_34_35_39;IntervalDuration=900_3600;BlockDuration=Daily;
        HistoryLength= 34128000;SubscriptionFrequency=Daily;
        AccountCollection=5;BR=1;")
    :ivar grant_types: [extension] Grant types this interface supports.
        (e.g. "client_credentials, authorization_code, refresh_token" in
        separate tags
    :ivar response_types: [extension] Response types supported. (e.g.
        "code")
    :ivar registration_client_uri: [extension] {ClientConfigurationURI}
        A URI used by a registered client to manage registration
        information.  This URI is returned by the AuthorizationServer in
        the “registration_client_uri” field of the client information
        response.
        {AuthorizationServerRegistrationEndpoint}/ApplicationInformation/{ApplicationInformationID}.
        (e.g.
        "https://server.example.com/DataCustodian/espi/1_1/resource/ApplicationInformation/{ApplicationInformationID}/")
    :ivar registration_access_token: [extension] A credential obtained
        during Third Party registration with the Data Custodian to
        enable access to the ApplicationInformation resource. This is
        persisted in the ApplicationInformation resource structure.
        (e.g. "fe82518d-e325-404e-978c-c02f9339bccc")
    :ivar data_custodian_scope_selection_screen_uri:
        [DEPRECATED][extension] The URI used by the Third Party to
        redirect the Retail Customer to the Data Custodian Scope
        Selection Screen (note that this will likely involve a dialog
        with the Retail Customer including a log in authentication
        process). (e.g.
        http://server.example.com/DataCustodian/RetailCustomer/ScopeSelection)
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    data_custodian_id: str = field(
        metadata={
            "name": "dataCustodianId",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    data_custodian_application_status: Union[
        int, DataCustodianApplicationStatusValue
    ] = field(
        metadata={
            "name": "dataCustodianApplicationStatus",
            "type": "Element",
            "required": True,
        }
    )
    third_party_application_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "thirdPartyApplicationDescription",
            "type": "Element",
            "max_length": 256,
        },
    )
    third_party_application_status: Optional[
        Union[int, ThirdPartyApplicatonStatusValue]
    ] = field(
        default=None,
        metadata={
            "name": "thirdPartyApplicationStatus",
            "type": "Element",
        },
    )
    third_party_application_type: Optional[
        Union[int, ThirdPartyApplicationTypeValue]
    ] = field(
        default=None,
        metadata={
            "name": "thirdPartyApplicationType",
            "type": "Element",
        },
    )
    third_party_application_use: Optional[
        Union[int, ThirdPartyApplicationUseValue]
    ] = field(
        default=None,
        metadata={
            "name": "thirdPartyApplicationUse",
            "type": "Element",
        },
    )
    third_party_phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "thirdPartyPhone",
            "type": "Element",
            "max_length": 32,
        },
    )
    authorization_server_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "authorizationServerUri",
            "type": "Element",
        },
    )
    third_party_notify_uri: str = field(
        metadata={
            "name": "thirdPartyNotifyUri",
            "type": "Element",
            "required": True,
        }
    )
    authorization_server_authorization_endpoint: str = field(
        metadata={
            "name": "authorizationServerAuthorizationEndpoint",
            "type": "Element",
            "required": True,
        }
    )
    authorization_server_registration_endpoint: Optional[str] = field(
        default=None,
        metadata={
            "name": "authorizationServerRegistrationEndpoint",
            "type": "Element",
        },
    )
    authorization_server_token_endpoint: str = field(
        metadata={
            "name": "authorizationServerTokenEndpoint",
            "type": "Element",
            "required": True,
        }
    )
    data_custodian_bulk_request_uri: str = field(
        metadata={
            "name": "dataCustodianBulkRequestURI",
            "type": "Element",
            "required": True,
        }
    )
    data_custodian_resource_endpoint: str = field(
        metadata={
            "name": "dataCustodianResourceEndpoint",
            "type": "Element",
            "required": True,
        }
    )
    third_party_scope_selection_screen_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "thirdPartyScopeSelectionScreenURI",
            "type": "Element",
        },
    )
    third_party_user_portal_screen_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "thirdPartyUserPortalScreenURI",
            "type": "Element",
        },
    )
    client_secret: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 512,
        }
    )
    logo_uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    client_name: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        }
    )
    client_uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    redirect_uri: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    client_id: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    tos_uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    policy_uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    software_id: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        }
    )
    software_version: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 32,
        }
    )
    client_id_issued_at: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    client_secret_expires_at: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    contacts: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )
    token_endpoint_auth_method: TokenEndPointMethod = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    scope: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_length": 256,
        },
    )
    grant_types: List[GrantType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
        },
    )
    response_types: ResponseType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    registration_client_uri: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    registration_access_token: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    data_custodian_scope_selection_screen_uri: Optional[object] = field(
        default=None,
        metadata={
            "name": "dataCustodianScopeSelectionScreenURI",
            "type": "Element",
        },
    )


class Authorization(IdentifiedObject):
    """[extension] Represents a permission granted by an owner for access to a
    resource.

    Atom Links:
    self link to this resource
    rel corresponding ApplicationInformation (if this is the client access containing token instance)
    rel corresponding to the authorized resource (if this is the access_token containing instance for a customer resource)
    Note: for privacy there is no identifier of the RetailCustomer in this structure but an implementation will have consider how to maintain a correspondence between a RetailCustomer and his authorization.

    :ivar authorized_period: Restricts access to requests or
        subscriptions within this date time interval. (e.g.
        "duration=31536000,start=1333252800", a duration value of "0"
        (zero) indicates an infinite duration period)
    :ivar published_period: Restricts access to the objects within the
        associated resource that were published within this date time
        interval. (e.g. "duration=31536000" for most recent 365 days)
    :ivar status: The status of this authorization. (e.g. "1" =&gt;
        active)
    :ivar expires_at: Expiration period for the access token. (e.g.
        "1403190000" for 2014-06-19T15:00:00Z)
    :ivar grant_type: Type of grant being negotiated for. (e.g.
        "authorization_code")
    :ivar scope: Negotiated scope of the authorization. (e.g.
        "FB=1_3_4_5_13_14_15_1937_39;IntervalDuration=3600;BlockDuration=monthly;HistoryLength=94608000"
    :ivar token_type: Type of token used. (e.g. "Bearer")
    :ivar error: Contains last error returned to ThirdParty. (e.g.
        "server_error")
    :ivar error_description: Contains free text string describing last
        error returned to ThirdParty. (e.g. "No Service")
    :ivar error_uri: Specific error URI for last returned error. (e.g.
        "na" if not supported)
    :ivar resource_uri: URI that can be used to access the EUI data the
        Third Party is authorized to access. Can be used in a GET of the
        EUI resource subscription (e.g.
        "http://server.example.com/DataCustodian/espi/1_1/resource/Batch/Subscription/1").
    :ivar authorization_uri: URI that can be used to update or delete
        this Authorization. (e.g.
        "http://server.example.com/DataCustodian/espi/1_1/resource/Authorization/1")
    :ivar customer_resource_uri: URI that can be used to access PII data
        the Third Party is authorized to access.  Can be used in a GET
        of the PII resource subscription (e.g.
        "http://server.example.com/DataCustodian/espi/1_1/resource/Batch/Subscription/2").
        Note: This URI will have a differnt namespace than the URI value
        found in the resourceURI element.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    authorized_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "authorizedPeriod",
            "type": "Element",
        },
    )
    published_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "publishedPeriod",
            "type": "Element",
        },
    )
    status: Union[int, AuthorizationStatusValue] = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    expires_at: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    grant_type: Optional[GrantType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scope: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 256,
        }
    )
    token_type: TokenType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    error: Optional[OauthError] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    error_description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 256,
        },
    )
    error_uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    resource_uri: str = field(
        metadata={
            "name": "resourceURI",
            "type": "Element",
            "required": True,
        }
    )
    authorization_uri: str = field(
        metadata={
            "name": "authorizationURI",
            "type": "Element",
            "required": True,
        }
    )
    customer_resource_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerResourceURI",
            "type": "Element",
        },
    )


class ElectricPowerQualitySummary(IdentifiedObject):
    """A summary of power quality events.

    This information represents a summary of power quality information
    typically required by customer facility energy management systems.
    It is not intended to satisfy the detailed requirements of power
    quality monitoring. All values are as defined by measurementProtocol
    during the period. The standards typically also give ranges of
    allowed values; the information attributes are the raw measurements,
    not the "yes/no" determination by the various standards. See
    referenced standards for definition, measurement protocol and
    period.

    :ivar flicker_plt: A measurement of long term Rapid Voltage Change
        in hundredths of a Volt. flickerPlt is derived from 2 hours of
        Pst values (12 values combined in cubic relationship).
    :ivar flicker_pst: flickerPst is a value measured over 10 minutes
        that characterizes the likelihood that the voltage fluctuations
        would result in perceptible light flicker. A value of 1.0 is
        designed to represent the level that 50% of people would
        perceive flicker in a 60 watt incandescent bulb. The value
        reported is represented as an integer in hundredths.
    :ivar harmonic_voltage: A measurement of the Harmonic Voltage during
        the period. For DC, distortion is with respect to a signal of
        zero Hz.
    :ivar long_interruptions: A count of Long Interruption events (as
        defined by measurementProtocol) during the summary interval
        period.
    :ivar mains_voltage: A measurement of the Mains [Signaling] Voltage
        during the summary interval period in uV.
    :ivar measurement_protocol: A reference to the source standard used
        as the measurement protocol definition. Examples are: 0 =
        “IEEE1519-2009” 1 = “EN50160”
    :ivar power_frequency: A measurement of the power frequency during
        the summary interval period in uHz.
    :ivar rapid_voltage_changes: A count of Rapid Voltage Change events
        during the summary interval period
    :ivar short_interruptions: A count of Short Interruption events
        during the summary interval period
    :ivar summary_interval: Interval of summary period
    :ivar supply_voltage_dips: A count of Supply Voltage Dip events
        during the summary interval period
    :ivar supply_voltage_imbalance: A count of Supply Voltage Imbalance
        events during the summary interval period
    :ivar supply_voltage_variations: A count of Supply Voltage
        Variations during the summary interval period
    :ivar temp_overvoltage: A count of Temporary Overvoltage events (as
        defined by measurementProtocol) during the summary interval
        period
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    flicker_plt: Optional[int] = field(
        default=None,
        metadata={
            "name": "flickerPlt",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    flicker_pst: Optional[int] = field(
        default=None,
        metadata={
            "name": "flickerPst",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    harmonic_voltage: Optional[int] = field(
        default=None,
        metadata={
            "name": "harmonicVoltage",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    long_interruptions: Optional[int] = field(
        default=None,
        metadata={
            "name": "longInterruptions",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    mains_voltage: Optional[int] = field(
        default=None,
        metadata={
            "name": "mainsVoltage",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    measurement_protocol: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementProtocol",
            "type": "Element",
        },
    )
    power_frequency: Optional[int] = field(
        default=None,
        metadata={
            "name": "powerFrequency",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    rapid_voltage_changes: Optional[int] = field(
        default=None,
        metadata={
            "name": "rapidVoltageChanges",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    short_interruptions: Optional[int] = field(
        default=None,
        metadata={
            "name": "shortInterruptions",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    summary_interval: DateTimeInterval = field(
        metadata={
            "name": "summaryInterval",
            "type": "Element",
            "required": True,
        }
    )
    supply_voltage_dips: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplyVoltageDips",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    supply_voltage_imbalance: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplyVoltageImbalance",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    supply_voltage_variations: Optional[int] = field(
        default=None,
        metadata={
            "name": "supplyVoltageVariations",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    temp_overvoltage: Optional[int] = field(
        default=None,
        metadata={
            "name": "tempOvervoltage",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )


class ElectricPowerUsageSummary(IdentifiedObject):
    """
    [DEPRECATED] Summary of usage for a billing period.

    :ivar billing_period: The billing period to which the included
        measurements apply. May also be an off-bill arbitrary period.
    :ivar bill_last_period: The amount of the bill for the referenced
        billingPeriod  in hundred-thousandths of the currency specified
        in the ReadingType for this reading (e.g., 840 = USD, US
        dollar).
    :ivar bill_to_date: If the summary contains data from a current
        period beyond the end of the referenced billingPeriod, the bill
        amount as of the date the summary is generated, in hundred-
        thousandths of the currency specified in the ReadingType for
        this reading. (e.g., 840 = USD, US dollar).
    :ivar cost_additional_last_period: Additional charges from the for
        the referenced billingPeriod, in hundred-thousandths of the
        currency specified in the ReadingType for this reading. (e.g.,
        840 = USD, US dollar).
    :ivar cost_additional_detail_last_period: [extension] Additional
        charges from the for the referenced billingPeriod which in total
        add up to costAdditionalLastPeriod.
    :ivar currency: The ISO 4217 code indicating the currency applicable
        to the bill amounts in the summary.
    :ivar overall_consumption_last_period: [extension] The amount of
        energy consumed in the lfor the referenced billingPeriod.
    :ivar current_billing_period_over_all_consumption: If the summary
        contains data from a current period beyond the end of the
        referenced billingPeriod, the total consumption for the billing
        period.
    :ivar current_day_last_year_net_consumption: If the summary contains
        data from a current period beyond the end of the referenced
        billingPeriod, the amount of energy consumed one year ago
        interpreted as same day of week same week of year (see ISO 8601)
        based on the day of the statusTimeStamp.
    :ivar current_day_net_consumption: If the summary contains data from
        a current period beyond the end of the referenced billingPeriod,
        net consumption for the current day (delivered - received) based
        on the day of the statusTimeStamp
    :ivar current_day_overall_consumption: If the summary contains data
        from a current period beyond the end of the referenced
        billingPeriod, overall energy consumption for the current day,
        based on the day of the statusTimeStamp.
    :ivar peak_demand: If the summary contains data from a current
        period beyond the end of the referenced billingPeriod, peak
        demand recorded for the current period.
    :ivar previous_day_last_year_overall_consumption: If the summary
        contains data from a current period beyond the end of the
        referenced billingPeriod, the amount of energy consumed on the
        previous day one year ago interpreted as same day of week same
        week of year (see ISO 8601) based on the day of the
        statusTimestamp.
    :ivar previous_day_net_consumption: If the summary contains data
        from a current period beyond the end of the referenced
        billingPeriod, net consumption for the previous day relative to
        the day of the statusTimestamp.
    :ivar previous_day_overall_consumption: If the summary contains data
        from a current period beyond the end of the referenced
        billingPeriod, the total consumption for the previous day based
        on the day of the statusTimestamp.
    :ivar quality_of_reading: Indication of the quality of the summary
        readings
    :ivar ratchet_demand: If the summary contains data from a current
        period beyond the end of the referenced billingPeriod, the
        current ratchet demand value for the ratchet demand over the
        ratchetDemandPeriod.
    :ivar ratchet_demand_period: The period over which the ratchet
        demand applies
    :ivar status_time_stamp: Date/Time status of this UsageSummary
    :ivar commodity: [extension] The commodity for this summary report
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    billing_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "billingPeriod",
            "type": "Element",
        },
    )
    bill_last_period: Optional[int] = field(
        default=None,
        metadata={
            "name": "billLastPeriod",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    bill_to_date: Optional[int] = field(
        default=None,
        metadata={
            "name": "billToDate",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    cost_additional_last_period: Optional[int] = field(
        default=None,
        metadata={
            "name": "costAdditionalLastPeriod",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    cost_additional_detail_last_period: List[LineItem] = field(
        default_factory=list,
        metadata={
            "name": "costAdditionalDetailLastPeriod",
            "type": "Element",
        },
    )
    currency: Optional[Union[int, CurrencyValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    overall_consumption_last_period: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "overallConsumptionLastPeriod",
            "type": "Element",
        },
    )
    current_billing_period_over_all_consumption: Optional[
        SummaryMeasurement
    ] = field(
        default=None,
        metadata={
            "name": "currentBillingPeriodOverAllConsumption",
            "type": "Element",
        },
    )
    current_day_last_year_net_consumption: Optional[SummaryMeasurement] = (
        field(
            default=None,
            metadata={
                "name": "currentDayLastYearNetConsumption",
                "type": "Element",
            },
        )
    )
    current_day_net_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentDayNetConsumption",
            "type": "Element",
        },
    )
    current_day_overall_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentDayOverallConsumption",
            "type": "Element",
        },
    )
    peak_demand: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "peakDemand",
            "type": "Element",
        },
    )
    previous_day_last_year_overall_consumption: Optional[
        SummaryMeasurement
    ] = field(
        default=None,
        metadata={
            "name": "previousDayLastYearOverallConsumption",
            "type": "Element",
        },
    )
    previous_day_net_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "previousDayNetConsumption",
            "type": "Element",
        },
    )
    previous_day_overall_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "previousDayOverallConsumption",
            "type": "Element",
        },
    )
    quality_of_reading: Optional[Union[int, QualityOfReadingValue]] = field(
        default=None,
        metadata={
            "name": "qualityOfReading",
            "type": "Element",
        },
    )
    ratchet_demand: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "ratchetDemand",
            "type": "Element",
        },
    )
    ratchet_demand_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "ratchetDemandPeriod",
            "type": "Element",
        },
    )
    status_time_stamp: int = field(
        metadata={
            "name": "statusTimeStamp",
            "type": "Element",
            "required": True,
        }
    )
    commodity: Optional[Union[int, CommodityKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class IntervalBlock(IdentifiedObject):
    """
    Time sequence of Readings of the same ReadingType.

    :ivar interval: Specifies the time period during which the contained
        readings were taken.
    :ivar interval_reading: One or more interval reading values measured
        by a meter or other asset.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    interval: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    interval_reading: List[IntervalReading] = field(
        default_factory=list,
        metadata={
            "name": "IntervalReading",
            "type": "Element",
        },
    )


class MeterReading(IdentifiedObject):
    """
    Set of values obtained from the meter.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)


class ProgramIdMappings(IdentifiedObject):
    """
    [extension] List of programIDmappings.

    :ivar program_id_mapping: [extension] single program id mapping
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    program_id_mapping: List["ProgramIdMappings.ProgramIdMapping"] = field(
        default_factory=list,
        metadata={
            "name": "programIdMapping",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    class ProgramIdMapping(BaseModel):
        """
        :ivar t_ouor_cppor_consumption_tier: Type of billing tariff
            profile uses
        :ivar code: Code (numeric value)
        :ivar name: Name associated with code
        :ivar note: Optional description of code
        """

        model_config = ConfigDict(defer_build=True)
        t_ouor_cppor_consumption_tier: TOuorCpporConsumptionTier = field(
            metadata={
                "name": "tOUorCPPorConsumptionTier",
                "type": "Element",
                "required": True,
            }
        )
        code: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        name: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        note: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )


class ReadingType(IdentifiedObject):
    """
    Characteristics associated with all Readings included in a MeterReading.

    :ivar accumulation_behaviour: Code indicating how value is
        accumulated over time for Readings of ReadingType.
    :ivar commodity: Code for commodity classification of Readings of
        ReadingType.
    :ivar consumption_tier: Code for consumption tier associated with a
        Reading of ReadingType.
    :ivar currency: Code for the currency for costs associated with this
        ReadingType.  The valid values per the standard are defined in
        CurrencyCode.
    :ivar data_qualifier: Code describing a salient attribute of
        Readings of ReadingType.
    :ivar default_quality: Default value to be used if no value of
        ReadingQuality.quality is provided. Specific format and valid
        values per the standard are specified in QualityOfReading.
    :ivar flow_direction: Direction associated with current related
        Readings.
    :ivar interval_length: Default interval length specified in seconds
        for Readings of ReadingType.
    :ivar kind: Code for general classification of a Reading of
        ReadingType.
    :ivar phase: Code for phase information associated with Readings of
        ReadingType.
    :ivar power_of_ten_multiplier: Code for the power of ten multiplier
        which, when used in combination with the uom, specifies the
        actual unit of measure for Readings of ReadingType.
    :ivar time_attribute: Code used to specify a particular type of time
        interval method for Readings of ReadingType.
    :ivar tou: Code for the TOU type of Readings of ReadingType.
    :ivar uom: Code for the base unit of measure for Readings of
        ReadingType.  Used in combination with the powerOfTenMultiplier
        to specify the actual unit of measure
    :ivar cpp: [extension] Critical peak period (CPP) bucket the reading
        value is attributed to. Value 0 means not applicable. Even
        though CPP is usually considered a specialized form of time of
        use 'tou', this attribute is defined explicitly for flexibility.
    :ivar interharmonic: [extension] Indication of a "harmonic" or
        "interharmonic" basis for the measurement. Value 0 in
        'numerator' and 'denominator' means not applicable.
    :ivar measuring_period: [extension] Time attribute inherent or
        fundamental to the reading value (as opposed to 'macroPeriod'
        that supplies an "adjective" to describe aspects of a time
        period with regard to the measurement). It refers to the way the
        value was originally measured and not to the frequency at which
        it is reported or presented. For example, an hourly interval of
        consumption data would have value 'hourly' as an attribute.
        However in the case of an hourly sampled voltage value, the
        meterReadings schema would carry the 'hourly' interval size
        information. It is common for meters to report demand in a form
        that is measured over the course of a portion of an hour, while
        enterprise applications however commonly assume the demand (in
        kW or kVAr) normalized to 1 hour. The system that receives
        readings directly from the meter therefore must perform this
        transformation before publishing readings for use by the other
        enterprise systems. The scalar used is chosen based on the block
        size (not any sub-interval size).
    :ivar argument: [extension] Argument used to introduce numbers into
        the unit of measure description where they are needed (e.g., 4
        where the measure needs an argument such as CEMI(n=4)). Most
        arguments used in practice however will be integers (i.e.,
        'denominator'=1). Value 0 in 'numerator' and 'denominator' means
        not applicable.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    accumulation_behaviour: Optional[Union[int, AccumulationKindValue]] = (
        field(
            default=None,
            metadata={
                "name": "accumulationBehaviour",
                "type": "Element",
            },
        )
    )
    commodity: Optional[Union[int, CommodityKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    consumption_tier: Optional[int] = field(
        default=None,
        metadata={
            "name": "consumptionTier",
            "type": "Element",
        },
    )
    currency: Optional[Union[int, CurrencyValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    data_qualifier: Optional[Union[int, DataQualifierKindValue]] = field(
        default=None,
        metadata={
            "name": "dataQualifier",
            "type": "Element",
        },
    )
    default_quality: Optional[Union[int, QualityOfReadingValue]] = field(
        default=None,
        metadata={
            "name": "defaultQuality",
            "type": "Element",
        },
    )
    flow_direction: Optional[Union[int, FlowDirectionKindValue]] = field(
        default=None,
        metadata={
            "name": "flowDirection",
            "type": "Element",
        },
    )
    interval_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "intervalLength",
            "type": "Element",
        },
    )
    kind: Optional[Union[int, MeasurementKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    phase: Optional[Union[int, PhaseCodeKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    power_of_ten_multiplier: Optional[Union[int, UnitMultiplierKindValue]] = (
        field(
            default=None,
            metadata={
                "name": "powerOfTenMultiplier",
                "type": "Element",
            },
        )
    )
    time_attribute: Optional[Union[int, TimePeriodOfInterestValue]] = field(
        default=None,
        metadata={
            "name": "timeAttribute",
            "type": "Element",
        },
    )
    tou: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    uom: Optional[Union[int, UnitSymbolKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cpp: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    interharmonic: Optional[ReadingInterharmonic] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    measuring_period: Optional[Union[int, TimeAttributeKindValue]] = field(
        default=None,
        metadata={
            "name": "measuringPeriod",
            "type": "Element",
        },
    )
    argument: Optional[RationalNumber] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class ServiceDeliveryPoint(Object):
    """
    [extension] Service Delivery Point is representation of revenue UsagePoint
    attributes.

    :ivar name: The name is any free human readable and possibly non
        unique text naming the object.
    :ivar tariff_profile: A schedule of charges; structure associated
        with Tariff that allows the definition of complex tariff
        structures such as step and time of use.
    :ivar customer_agreement: Agreement between the customer and the
        ServiceSupplier to pay for service at a specific service
        location. It provides for the recording of certain billing
        information about the type of service provided at the service
        location and is used during charge creation to determine the
        type of service.
    :ivar tariff_rider_refs: [extension] List of rate options applied to
        the base tariff profile
    """

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        },
    )
    tariff_profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "tariffProfile",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        },
    )
    customer_agreement: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerAgreement",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "max_length": 256,
        },
    )
    tariff_rider_refs: Optional[TariffRiderRefs] = field(
        default=None,
        metadata={
            "name": "tariffRiderRefs",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
        },
    )


class TimeConfiguration(IdentifiedObject):
    """
    [extension] Contains attributes related to the configuration of the time
    service.

    :ivar dst_end_rule: Rule to calculate end of daylight savings time
        in the current year.  Result of dstEndRule must be greater than
        result of dstStartRule.
    :ivar dst_offset: Daylight savings time offset from local standard
        time.
    :ivar dst_start_rule: Rule to calculate start of daylight savings
        time in the current year. Result of dstEndRule must be greater
        than result of dstStartRule.
    :ivar tz_offset: Local time zone offset from UTCTime. Does not
        include any daylight savings time offsets.
    """

    model_config = ConfigDict(defer_build=True)
    dst_end_rule: bytes = field(
        metadata={
            "name": "dstEndRule",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 4,
            "format": "base16",
        }
    )
    dst_offset: int = field(
        metadata={
            "name": "dstOffset",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )
    dst_start_rule: bytes = field(
        metadata={
            "name": "dstStartRule",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
            "max_length": 4,
            "format": "base16",
        }
    )
    tz_offset: int = field(
        metadata={
            "name": "tzOffset",
            "type": "Element",
            "namespace": "http://naesb.org/espi",
            "required": True,
        }
    )


class UsageSummary(IdentifiedObject):
    """
    [extension] Summary of usage for a billing period.

    :ivar billing_period: The billing period to which the included
        measurements apply. May also be an off-bill arbitrary period.
    :ivar bill_last_period: The amount of the bill for the referenced
        billingPeriod  in hundred-thousandths of the currency specified
        in the ReadingType for this reading (e.g., 840 = USD, US
        dollar).
    :ivar bill_to_date: If the summary contains data from a current
        period beyond the end of the referenced billingPeriod, the bill
        amount as of the date the summary is generated, in hundred-
        thousandths of the currency specified in the ReadingType for
        this reading. (e.g., 840 = USD, US dollar).
    :ivar cost_additional_last_period: Additional charges from the for
        the referenced billingPeriod, in hundred-thousandths of the
        currency specified in the ReadingType for this reading. (e.g.,
        840 = USD, US dollar).
    :ivar cost_additional_detail_last_period: [extension] Additional
        charges from the for the referenced billingPeriod which in total
        add up to costAdditionalLastPeriod.
    :ivar currency: The ISO 4217 code indicating the currency applicable
        to the bill amounts in the summary.
    :ivar overall_consumption_last_period: [extension] The amount of
        energy consumed in the lfor the referenced billingPeriod.
    :ivar current_billing_period_over_all_consumption: If the summary
        contains data from a current period beyond the end of the
        referenced billingPeriod, the total consumption for the billing
        period.
    :ivar current_day_last_year_net_consumption: If the summary contains
        data from a current period beyond the end of the referenced
        billingPeriod, the amount of energy consumed one year ago
        interpreted as same day of week same week of year (see ISO 8601)
        based on the day of the statusTimeStamp.
    :ivar current_day_net_consumption: If the summary contains data from
        a current period beyond the end of the referenced billingPeriod,
        net consumption for the current day (delivered - received) based
        on the day of the statusTimeStamp
    :ivar current_day_overall_consumption: If the summary contains data
        from a current period beyond the end of the referenced
        billingPeriod, overall energy consumption for the current day,
        based on the day of the statusTimeStamp.
    :ivar peak_demand: If the summary contains data from a current
        period beyond the end of the referenced billingPeriod, peak
        demand recorded for the current period.
    :ivar previous_day_last_year_overall_consumption: If the summary
        contains data from a current period beyond the end of the
        referenced billingPeriod, the amount of energy consumed on the
        previous day one year ago interpreted as same day of week same
        week of year (see ISO 8601) based on the day of the
        statusTimestamp.
    :ivar previous_day_net_consumption: If the summary contains data
        from a current period beyond the end of the referenced
        billingPeriod, net consumption for the previous day relative to
        the day of the statusTimestamp.
    :ivar previous_day_overall_consumption: If the summary contains data
        from a current period beyond the end of the referenced
        billingPeriod, the total consumption for the previous day based
        on the day of the statusTimestamp.
    :ivar quality_of_reading: Indication of the quality of the summary
        readings
    :ivar ratchet_demand: If the summary contains data from a current
        period beyond the end of the referenced billingPeriod, the
        current ratchet demand value for the ratchet demand over the
        ratchetDemandPeriod.
    :ivar ratchet_demand_period: The period over which the ratchet
        demand applies
    :ivar status_time_stamp: Date/Time status of this UsageSummary
    :ivar commodity: [extension] The commodity for this summary report
    :ivar tariff_profile: [extension] A schedule of charges; structure
        associated with Tariff that allows the definition of complex
        tariff structures such as step and time of use.
    :ivar read_cycle: [extension] Cycle day on which the meter for this
        usage point will normally be read.  Usually correlated with the
        billing cycle.
    :ivar tariff_rider_refs: [extension] List of rate options applied to
        the base tariff profile
    :ivar billing_charge_source: [extension] Source of Billing Charge
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    billing_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "billingPeriod",
            "type": "Element",
        },
    )
    bill_last_period: Optional[int] = field(
        default=None,
        metadata={
            "name": "billLastPeriod",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    bill_to_date: Optional[int] = field(
        default=None,
        metadata={
            "name": "billToDate",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    cost_additional_last_period: Optional[int] = field(
        default=None,
        metadata={
            "name": "costAdditionalLastPeriod",
            "type": "Element",
            "min_inclusive": -140737488355328,
            "max_inclusive": 140737488355328,
        },
    )
    cost_additional_detail_last_period: List[LineItem] = field(
        default_factory=list,
        metadata={
            "name": "costAdditionalDetailLastPeriod",
            "type": "Element",
        },
    )
    currency: Optional[Union[int, CurrencyValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    overall_consumption_last_period: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "overallConsumptionLastPeriod",
            "type": "Element",
        },
    )
    current_billing_period_over_all_consumption: Optional[
        SummaryMeasurement
    ] = field(
        default=None,
        metadata={
            "name": "currentBillingPeriodOverAllConsumption",
            "type": "Element",
        },
    )
    current_day_last_year_net_consumption: Optional[SummaryMeasurement] = (
        field(
            default=None,
            metadata={
                "name": "currentDayLastYearNetConsumption",
                "type": "Element",
            },
        )
    )
    current_day_net_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentDayNetConsumption",
            "type": "Element",
        },
    )
    current_day_overall_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "currentDayOverallConsumption",
            "type": "Element",
        },
    )
    peak_demand: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "peakDemand",
            "type": "Element",
        },
    )
    previous_day_last_year_overall_consumption: Optional[
        SummaryMeasurement
    ] = field(
        default=None,
        metadata={
            "name": "previousDayLastYearOverallConsumption",
            "type": "Element",
        },
    )
    previous_day_net_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "previousDayNetConsumption",
            "type": "Element",
        },
    )
    previous_day_overall_consumption: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "previousDayOverallConsumption",
            "type": "Element",
        },
    )
    quality_of_reading: Optional[Union[int, QualityOfReadingValue]] = field(
        default=None,
        metadata={
            "name": "qualityOfReading",
            "type": "Element",
        },
    )
    ratchet_demand: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "ratchetDemand",
            "type": "Element",
        },
    )
    ratchet_demand_period: Optional[DateTimeInterval] = field(
        default=None,
        metadata={
            "name": "ratchetDemandPeriod",
            "type": "Element",
        },
    )
    status_time_stamp: int = field(
        metadata={
            "name": "statusTimeStamp",
            "type": "Element",
            "required": True,
        }
    )
    commodity: Optional[Union[int, CommodityKindValue]] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tariff_profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "tariffProfile",
            "type": "Element",
            "max_length": 256,
        },
    )
    read_cycle: Optional[str] = field(
        default=None,
        metadata={
            "name": "readCycle",
            "type": "Element",
            "max_length": 256,
        },
    )
    tariff_rider_refs: Optional[TariffRiderRefs] = field(
        default=None,
        metadata={
            "name": "tariffRiderRefs",
            "type": "Element",
        },
    )
    billing_charge_source: Optional[BillingChargeSource] = field(
        default=None,
        metadata={
            "name": "billingChargeSource",
            "type": "Element",
        },
    )


class LocalTimeParameters(TimeConfiguration):
    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)


class UsagePoint(IdentifiedObject):
    """
    Logical point on a network at which consumption or production is either
    physically measured (e.g., metered) or estimated (e.g., unmetered street
    lights).

    :ivar role_flags: Specifies the roles that this usage point has been
        assigned. Bit 1 - isMirror Bit 2 - isPremisesAggregationPoint
        Bit 3 - isPEV Bit 4 - isDER Bit 5 - isRevenueQuality Bit 6 -
        isDC Bit 7-16 - Reserved
    :ivar service_category: Category of service provided to the
        customer.
    :ivar status: Specifies the current status of this usage point.
        Valid values include: 0 = off 1 = on
    :ivar service_delivery_point: [extension] Contains service delivery
        point information about the UsagePoint if it does represent the
        service delivery point.
    :ivar ami_billing_ready: [extension] Tracks the lifecycle of the
        metering installation at a usage point with respect to readiness
        for billing via advanced metering infrastructure reads.
    :ivar check_billing: [extension] True if as a result of an
        inspection or otherwise, there is a reason to suspect that a
        previous billing may have been performed with erroneous data.
        Value should be reset once this potential discrepancy has been
        resolved.
    :ivar connection_state: [extension] State of the usage point with
        respect to connection to the network.
    :ivar estimated_load: [extension] Estimated load.
    :ivar grounded: [extension] True if grounded.
    :ivar is_sdp: [extension] If true, this usage point is a service
        delivery point, i.e., a usage point where the ownership of the
        service changes hands.
    :ivar is_virtual: [extension] If true, this usage point is virtual,
        i.e., no physical location exists in the network where a meter
        could be located to collect the meter readings. For example, one
        may define a virtual usage point to serve as an aggregation of
        usage for all of a company's premises distributed widely across
        the distribution territory. Otherwise, the usage point is
        physical, i.e., there is a logical point in the network where a
        meter could be located to collect meter readings.
    :ivar minimal_usage_expected: [extension] If true, minimal or zero
        usage is expected at this usage point for situations such as
        premises vacancy, logical or physical disconnect. It is used for
        readings validation and estimation.
    :ivar nominal_service_voltage: [extension] Nominal service voltage.
    :ivar outage_region: [extension] Outage region in which this usage
        point is located.
    :ivar phase_code: [extension] Phase code. Number of wires and
        specific nominal phases can be deduced from enumeration literal
        values. For example, ABCN is three-phase, four-wire, s12n
        (splitSecondary12N) is single-phase, three-wire, and s1n and s2n
        are single-phase, two-wire.
    :ivar rated_current: [extension] Current flow that this usage point
        is configured to deliver.
    :ivar rated_power: [extension] Active power that this usage point is
        configured to deliver.
    :ivar read_cycle: [extension] Cycle day on which the meter for this
        usage point will normally be read.  Usually correlated with the
        billing cycle.
    :ivar read_route: [extension] Identifier of the route to which this
        usage point is assigned for purposes of meter reading. Typically
        used to configure hand held meter reading systems prior to
        collection of reads.
    :ivar service_delivery_remark: [extension] Remarks about this usage
        point, for example the reason for it being rated with a non-
        nominal priority.
    :ivar service_priority: [extension] Priority of service for this
        usage point. Note that usage points at the same service location
        can have different priorities.
    :ivar pnode_refs: [extension] A single electrical system Node or
        subset of Nodes where a physical injection or withdrawal of
        electricity is modeled and for which a Locational Marginal Price
        is calculated by the RTO/ISO and used for financial settlements.
    :ivar aggregate_node_refs: [extension] A sequence of references to
        AggregateNodes.
    """

    class Meta:
        namespace = "http://naesb.org/espi"

    model_config = ConfigDict(defer_build=True)
    role_flags: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "roleFlags",
            "type": "Element",
            "max_length": 2,
            "format": "base16",
        },
    )
    service_category: Optional[ServiceCategory] = field(
        default=None,
        metadata={
            "name": "ServiceCategory",
            "type": "Element",
        },
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    service_delivery_point: Optional[ServiceDeliveryPoint] = field(
        default=None,
        metadata={
            "name": "serviceDeliveryPoint",
            "type": "Element",
        },
    )
    ami_billing_ready: Optional[AmiBillingReadyKind] = field(
        default=None,
        metadata={
            "name": "amiBillingReady",
            "type": "Element",
        },
    )
    check_billing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "checkBilling",
            "type": "Element",
        },
    )
    connection_state: Optional[UsagePointConnectedKind] = field(
        default=None,
        metadata={
            "name": "connectionState",
            "type": "Element",
        },
    )
    estimated_load: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "estimatedLoad",
            "type": "Element",
        },
    )
    grounded: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    is_sdp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSdp",
            "type": "Element",
        },
    )
    is_virtual: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isVirtual",
            "type": "Element",
        },
    )
    minimal_usage_expected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "minimalUsageExpected",
            "type": "Element",
        },
    )
    nominal_service_voltage: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "nominalServiceVoltage",
            "type": "Element",
        },
    )
    outage_region: Optional[str] = field(
        default=None,
        metadata={
            "name": "outageRegion",
            "type": "Element",
            "max_length": 256,
        },
    )
    phase_code: Optional[Union[int, PhaseCodeKindValue]] = field(
        default=None,
        metadata={
            "name": "phaseCode",
            "type": "Element",
        },
    )
    rated_current: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "ratedCurrent",
            "type": "Element",
        },
    )
    rated_power: Optional[SummaryMeasurement] = field(
        default=None,
        metadata={
            "name": "ratedPower",
            "type": "Element",
        },
    )
    read_cycle: Optional[str] = field(
        default=None,
        metadata={
            "name": "readCycle",
            "type": "Element",
            "max_length": 256,
        },
    )
    read_route: Optional[str] = field(
        default=None,
        metadata={
            "name": "readRoute",
            "type": "Element",
            "max_length": 256,
        },
    )
    service_delivery_remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceDeliveryRemark",
            "type": "Element",
            "max_length": 256,
        },
    )
    service_priority: Optional[str] = field(
        default=None,
        metadata={
            "name": "servicePriority",
            "type": "Element",
            "max_length": 32,
        },
    )
    pnode_refs: Optional[PnodeRefs] = field(
        default=None,
        metadata={
            "name": "pnodeRefs",
            "type": "Element",
        },
    )
    aggregate_node_refs: Optional[AggregateNodeRefs] = field(
        default=None,
        metadata={
            "name": "aggregateNodeRefs",
            "type": "Element",
        },
    )
