import pymem
import keyboard
import time

#Update these every CS:GO update
cs_gamerules_data = (0x0)
m_ArmorValue = (0xB378)
m_Collision = (0x320)
m_CollisionGroup = (0x474)
m_Local = (0x2FBC)
m_MoveType = (0x25C)
m_OriginalOwnerXuidHigh = (0x31C4)
m_OriginalOwnerXuidLow = (0x31C0)
m_SurvivalGameRuleDecisionTypes = (0x1320)
m_SurvivalRules = (0xCF8)
m_aimPunchAngle = (0x302C)
m_aimPunchAngleVel = (0x3038)
m_angEyeAnglesX = (0xB37C)
m_angEyeAnglesY = (0xB380)
m_bBombPlanted = (0x99D)
m_bFreezePeriod = (0x20)
m_bGunGameImmunity = (0x3944)
m_bHasDefuser = (0xB388)
m_bHasHelmet = (0xB36C)
m_bInReload = (0x32A5)
m_bIsDefusing = (0x3930)
m_bIsQueuedMatchmaking = (0x74)
m_bIsScoped = (0x3928)
m_bIsValveDS = (0x75)
m_bSpotted = (0x93D)
m_bSpottedByMask = (0x980)
m_bStartedArming = (0x33F0)
m_bUseCustomAutoExposureMax = (0x9D9)
m_bUseCustomAutoExposureMin = (0x9D8)
m_bUseCustomBloomScale = (0x9DA)
m_clrRender = (0x70)
m_dwBoneMatrix = (0x26A8)
m_fAccuracyPenalty = (0x3330)
m_fFlags = (0x104)
m_flC4Blow = (0x2990)
m_flCustomAutoExposureMax = (0x9E0)
m_flCustomAutoExposureMin = (0x9DC)
m_flCustomBloomScale = (0x9E4)
m_flDefuseCountDown = (0x29AC)
m_flDefuseLength = (0x29A8)
m_flFallbackWear = (0x31D0)
m_flFlashDuration = (0xA420)
m_flFlashMaxAlpha = (0xA41C)
m_flLastBoneSetupTime = (0x2924)
m_flLowerBodyYawTarget = (0x3A90)
m_flNextAttack = (0x2D70)
m_flNextPrimaryAttack = (0x3238)
m_flSimulationTime = (0x268)
m_flTimerLength = (0x2994)
m_hActiveWeapon = (0x2EF8)
m_hMyWeapons = (0x2DF8)
m_hObserverTarget = (0x338C)
m_hOwner = (0x29CC)
m_hOwnerEntity = (0x14C)
m_iAccountID = (0x2FC8)
m_iClip1 = (0x3264)
m_iCompetitiveRanking = (0x1A84)
m_iCompetitiveWins = (0x1B88)
m_iCrosshairId = (0xB3E4)
m_iEntityQuality = (0x2FAC)
m_iFOV = (0x31E4)
m_iFOVStart = (0x31E8)
m_iGlowIndex = (0xA438)
m_iHealth = (0x100)
m_iItemDefinitionIndex = (0x2FAA)
m_iItemIDHigh = (0x2FC0)
m_iMostRecentModelBoneCounter = (0x2690)
m_iObserverMode = (0x3378)
m_iShotsFired = (0xA390)
m_iState = (0x3258)
m_iTeamNum = (0xF4)
m_lifeState = (0x25F)
m_nFallbackPaintKit = (0x31C8)
m_nFallbackSeed = (0x31CC)
m_nFallbackStatTrak = (0x31D4)
m_nForceBone = (0x268C)
m_nTickBase = (0x3430)
m_rgflCoordinateFrame = (0x444)
m_szCustomName = (0x303C)
m_szLastPlaceName = (0x35B4)
m_thirdPersonViewAngles = (0x31D8)
m_vecOrigin = (0x138)
m_vecVelocity = (0x114)
m_vecViewOffset = (0x108)
m_viewPunchAngle = (0x3020)
anim_overlays = (0x2980)
clientstate_choked_commands = (0x4D28)
clientstate_delta_ticks = (0x174)
clientstate_last_outgoing_command = (0x4D24)
clientstate_net_channel = (0x9C)
convar_name_hash_table = (0x2F0F8)
dwClientState = (0x58ADD4)
dwClientState_GetLocalPlayer = (0x180)
dwClientState_IsHLTV = (0x4D40)
dwClientState_Map = (0x28C)
dwClientState_MapDirectory = (0x188)
dwClientState_MaxPlayer = (0x388)
dwClientState_PlayerInfo = (0x52B8)
dwClientState_State = (0x108)
dwClientState_ViewAngles = (0x4D88)
dwEntityList = (0x4D5450C)
dwForceAttack = (0x3185AA0)
dwForceAttack2 = (0x3185AAC)
dwForceBackward = (0x3185A58)
dwForceForward = (0x3185A64)
dwForceJump = (0x51FE22C)
dwForceLeft = (0x3185A7C)
dwForceRight = (0x3185A70)
dwGameDir = (0x629678)
dwGameRulesProxy = (0x527151C)
dwGetAllClasses = (0xD662BC)
dwGlobalVars = (0x58AAD8)
dwGlowObjectManager = (0x529C3D8)
dwInput = (0x51A5AE8)
dwInterfaceLinkList = (0x9087D4)
dwLocalPlayer = (0xD3FC5C)
dwMouseEnable = (0xD45800)
dwMouseEnablePtr = (0xD457D0)
dwPlayerResource = (0x3183DF0)
dwRadarBase = (0x518927C)
dwSensitivity = (0xD4569C)
dwSensitivityPtr = (0xD45670)
dwSetClanTag = (0x89FB0)
dwViewMatrix = (0x4D45E54)
dwWeaponTable = (0x51A65A8)
dwWeaponTableIndex = (0x325C)
dwYawPtr = (0xD45460)
dwZoomSensitivityRatioPtr = (0xD4A700)
dwbSendPackets = (0xD423A)
dwppDirect3DDevice9 = (0xA7030)
find_hud_element = (0x30034310)
force_update_spectator_glow = (0x3A3242)
interface_engine_cvar = (0x3E9EC)
is_c4_owner = (0x3AFCD0)
m_bDormant = (0xED)
m_flSpawnTime = (0xA370)
m_pStudioHdr = (0x294C)
m_pitchClassPtr = (0x5189518)
m_yawClassPtr = (0xD45460)
model_ambient_min = (0x58DE4C)
set_abs_angles = (0x1D7110)
set_abs_origin = (0x1D6F50)



def glow():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        if keyboard.is_pressed('delete'):
            exit(0)


        glow_manager = pm.read_int(client + dwGlowObjectManager)
        for i in range(1, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                #Uses normal RGBA (RED,GREEN,BLUE,ALPHA) Color Input. Use wanted Value devided by 255 Formula
                if entity_team == 2:
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(255 / 255)) #R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0 / 255)) #G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0 / 255)) #B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(255 / 255)) #A
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)
                    
                elif entity_team == 3:
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0 / 255)) #R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0 / 255) #G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(255 / 255)) #B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(255 / 255)) #A
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)

if __name__ == '__main__':
    glow()
