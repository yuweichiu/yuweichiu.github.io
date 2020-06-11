import pandas as pd

# This two list should have the same of total count of Gp:
MIX_RUN_ADI = pd.read_csv('mix_run_ADI.csv')  # Gp, Stage_name, groupname, chartname
MIX_RUN_AEI = pd.read_csv('mix_run_AEI.csv')  # Gp, Stage_name, groupname, chartname

ope_df = pd.read_csv("operation_no.csv")  # Operation_No, Stage
coatereqplist = pd.read_csv("coatereqlist.csv")  # Coater_ID
coater_type = pd.read_csv("coater_type.csv") # Coater_Type

GP_2_STAGE_NAME = MIX_RUN_ADI.drop_duplicates(subset=["Gp", "Stage_name"])
GP_TOTAL = GP_2_STAGE_NAME["Gp"].unique().tolist()

# In[]
adi_gp_dict = {}
for gi, gp in enumerate(GP_TOTAL)):
    this_gp = MIX_RUN_ADI[MIX_RUN_ADI["Gp"] == gp]
    num_of_this_gp = this_gp.shape[0]
    adi_in_each_gp_dict = {}
    stagename = this_gp.loc[0][0]  # need check the type of variable

    for notg in range(num_of_this_gp):
        adi_in_diff_spc_group_dict = {}
        groupname = this_gp.loc[notg][1]
        chartname = this_gp.loc[notg][2]

        if groupname == "N/A":
            adi_in_diff_spc_group_dict["df"] = "N/A"
            adi_in_diff_spc_group_dict["Message"] = "Didn't have the SPC group name of stage {0:s}.".format(stagename)
        else:
            spc_temp = dao.query(...)
            if spc_temp.shape[0] == 0:
                adi_in_diff_spc_group_dict["df"] = "N/A"
                adi_in_diff_spc_group_dict["Message"] = "The stage {0:s} do not contain any data.".format(stagename)
            else:
                adi_in_diff_spc_group_dict["df"] = spc_temp
                adi_in_diff_spc_group_dict["Message"] = "Query data successfully."

        adi_in_each_gp_dict[groupname] = adi_in_diff_spc_group_dict

    adi_gp_dict[gp] = adi_in_each_gp_dict


aei_gp_dict = {}
# do as adi do...

# In[]
align_ADI_2_AEI_collector = []
align_2_coater_collector = []

for gi, gp in enumerate(GP_TOTAL):
    this_gp = MIX_RUN_ADI[MIX_RUN_ADI["Gp"] == gp]
    stagename = GP_2_STAGE_NAME[GP_2_STAGE_NAME["Gp"] == gp]["Stage_Name"].str  # need check the type of variable
    groupname_list = this_gp[["groupname"]].values.tolist()

    # adi:
    adi_gp_df = None
    adi_gp_df_collector = []
    for spc_gp_id in range(len(groupname_list)):
        spc_group_name = groupname_list[spc_gp_id]
        df_in_dict = adi_gp_dict[gp][spc_group_name]["df"]
        if df_in_dict == "N/A":
            pass
        else:
            adi_gp_df_collector.append(df_in_dict)

    if len(adi_gp_df_collector) == 1:
        adi_gp_df = adi_gp_df_collector[0]
    else:
        adi_gp_df = pd.concat(adi_gp_df_collector, axis=0)  # need to check index should reset or not

    # aei:
    # do as adi ...

    # merging ADI to AEI
    # ...
    merge_AEI_ADI = pd.merge(AEI, ADI, on="")
    align_ADI_2_AEI_collector.append(merge_AEI_ADI)

    # merging with coaterdf under same stage
    # ...
    merge_coater = pd.merge(merge_AEI_ADI, cot_ope)
    align_ADI_2_AEI_collector.append(merge_coater)
    