--Shrine of the Kings

local s,id,o=GetID()
function s.initial_effect(c)

	--Activate
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	c:RegisterEffect(e1)

	-- ①: Activate Trap Card the turn it was Set
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,0))
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_TRAP_ACT_IN_SET_TURN)
	e2:SetProperty(EFFECT_FLAG_SET_AVAILABLE)
	e2:SetRange(LOCATION_FZONE)
	e2:SetTargetRange(LOCATION_SZONE,0)
	e2:SetCountLimit(1,id)
	e2:SetCondition(s.trapcon)
	c:RegisterEffect(e2)

	-- ②: If "Serket" is controlled, allow up to 2 more Trap activations
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,1))
	e3:SetType(EFFECT_TYPE_FIELD)
	e3:SetCode(EFFECT_TRAP_ACT_IN_SET_TURN)
	e3:SetProperty(EFFECT_FLAG_SET_AVAILABLE)
	e3:SetRange(LOCATION_SZONE)
	e3:SetTargetRange(LOCATION_SZONE,0)
	e3:SetCountLimit(2,id+1)
	e3:SetCondition(s.serketcon)
	c:RegisterEffect(e3)

	-- ③: Opponent cannot activate cards/effects in Battle Phase if "Illusion Beast of Serket" is present
	local e4=Effect.CreateEffect(c)
	e4:SetType(EFFECT_TYPE_FIELD)
	e4:SetCode(EFFECT_CANNOT_ACTIVATE)
	e4:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e4:SetTargetRange(0,1)
	e4:SetRange(LOCATION_FZONE)
	e4:SetValue(1)
	e4:SetCondition(s.actcon)
	c:RegisterEffect(e4)

	--Banish to Destroy 1 Spell/Trap
	local e5=Effect.CreateEffect(c)
	e5:SetDescription(aux.Stringid(id,2))
	e5:SetCategory(CATEGORY_DESTROY)
	e5:SetType(EFFECT_TYPE_IGNITION)
	e5:SetRange(LOCATION_GRAVE)
	e5:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e5:SetCountLimit(1,id)
	e5:SetCondition(aux.exccon)
	e5:SetCost(aux.bfgcost)
	e5:SetTarget(s.destg)
	e5:SetOperation(s.activate)
	c:RegisterEffect(e5)
end

-- Check if a "Serket" monster is controlled to allow additional Trap activations
function s.serketfilter(c)
	return c:IsFaceup() and c:IsCode(130000606)
end

function s.serketcon(e)
	local tp=e:GetHandlerPlayer()
	return Duel.IsExistingMatchingCard(s.serketfilter,tp,LOCATION_MZONE,0,1,nil)
end

-- Trap activation condition: No special condition for base effect
function s.trapcon(e)
	return true
end

-- Battle Phase activation restriction if "Illusion Beast of Serket" is present
function s.actcon(e)
	local ph=Duel.GetCurrentPhase()
	local tp=e:GetHandlerPlayer()
	return Duel.IsExistingMatchingCard(s.serketfilter,tp,LOCATION_MZONE,0,1,nil)
			and ph>=PHASE_BATTLE_START and ph<=PHASE_BATTLE
end

function s.serket_fusion_filter(c)
	return c:IsCode(130000622, 130000623, 130000624, 130000625)
end

-- Banish to Destroy 1 Spell/Trap
function s.activate(e,tp,eg,ep,ev,re,r,rp)
	local tc=Duel.GetFirstTarget()
	if tc:IsRelateToEffect(e) then
		Duel.Destroy(tc,REASON_EFFECT)
	end
end

function s.filter2(c)
	return c:IsFaceup() and c:IsType(TYPE_SPELL+TYPE_TRAP)
end

function s.destg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsOnField() and s.filter2(chkc) and chkc~=e:GetHandler() end
	if chk==0 then return Duel.IsExistingTarget(s.filter2,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,e:GetHandler()) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
	local g=Duel.SelectTarget(tp,s.filter2,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,1,e:GetHandler())
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
end