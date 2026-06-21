--Cruel Gate Guardian
local s,id=GetID()

-- Card codes
local CODE_SANGA   = 26202165
local CODE_KAZEJIN = 62340868
local CODE_SUIJIN  = 98434877

function s.initial_effect(c)
	-- Custom Xyz Summon (3+ materials; can use Sanga/Kazejin/Suijin from S/T Zone)
	c:EnableReviveLimit()
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetRange(LOCATION_EXTRA)
	e1:SetCondition(s.xyzcon)
	e1:SetTarget(s.xyztg)
	e1:SetOperation(s.xyzop)
	e1:SetValue(SUMMON_TYPE_XYZ)
	c:RegisterEffect(e1)

	-- (Quick) Detach 1; negate 1 face-up opponent's card, also banish if Sanga/Kazejin/Suijin was detached
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_DISABLE+CATEGORY_REMOVE)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetCode(EVENT_FREE_CHAIN)
	e2:SetRange(LOCATION_MZONE)
	e2:SetCountLimit(1,id)
	e2:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_MAIN_END)
	e2:SetCost(s.ngcost)
	e2:SetTarget(s.ngtg)
	e2:SetOperation(s.ngop)
	c:RegisterEffect(e2)

	-- If destroyed by battle or effect: SS 1 Level 9 "Gate Guardian" monster from Extra Deck, ignoring conditions
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,2))
	e3:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e3:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e3:SetCode(EVENT_DESTROYED)
	e3:SetProperty(EFFECT_FLAG_DELAY)
	e3:SetCondition(s.spcon)
	e3:SetTarget(s.sptg)
	e3:SetOperation(s.spop)
	c:RegisterEffect(e3)
end

--========================
-- Xyz Summon Procedure
--========================

-- Level 7 face-up monsters in MZONE (normal Xyz materials)
function s.mfilterM(c,xyzc)
	return c:IsFaceup() and c:IsLocation(LOCATION_MZONE) and c:IsLevel(7)
		and c:IsCanBeXyzMaterial(xyzc)
end

-- Permission: allow using these from S/T Zone (face-up, any type)
function s.mfilterS(c)
	return c:IsFaceup() and c:IsLocation(LOCATION_SZONE)
		and c:IsCode(CODE_SANGA,CODE_KAZEJIN,CODE_SUIJIN)
end

-- Group goal: at least 3 total; Extra Deck zone free; must-material checks pass
local function xyz_goal(sg,tp,xyzc)
	if #sg<3 then return false end
	if Duel.GetLocationCountFromEx(tp,tp,sg,xyzc)<=0 then return false end
	-- Respect "must be Xyz material" constraints if any exist
	-- (Auxiliary.MustMaterialCheck exists in your procedures)
	if not Auxiliary.MustMaterialCheck(sg,tp,EFFECT_MUST_BE_XMATERIAL) then return false end
	return true
end

function s.xyzcon(e,c,og,min,max)
	if c==nil then return true end
	local tp=c:GetControler()
	-- Collect candidates
	local mgM=Duel.GetMatchingGroup(s.mfilterM,tp,LOCATION_MZONE,0,nil,c)
	local mgS=Duel.GetMatchingGroup(s.mfilterS,tp,LOCATION_SZONE,0,nil)
	local mg=mgM:Clone()
	if #mgS>0 then mg:Merge(mgS) end
	-- Quick pre-check
	if #mg<3 then return false end
	-- Must-material rule cards
	local sg=Duel.GetMustMaterial(tp,EFFECT_MUST_BE_XMATERIAL)
	if #sg>0 and sg:IsExists(function(x) return not mg:IsContains(x) end,1,nil) then
		return false
	end
	-- Can we find any valid subgroup?
	Duel.SetSelectedCard(sg)
	return mg:CheckSubGroup(xyz_goal,3,99,tp,c)
end

function s.xyztg(e,tp,eg,ep,ev,re,r,rp,chk,c,og,min,max)
	local tp=c:GetControler()
	local mgM=Duel.GetMatchingGroup(s.mfilterM,tp,LOCATION_MZONE,0,nil,c)
	local mgS=Duel.GetMatchingGroup(s.mfilterS,tp,LOCATION_SZONE,0,nil)
	local mg=mgM:Clone()
	if #mgS>0 then mg:Merge(mgS) end
	-- Must-material rule cards
	local must=Duel.GetMustMaterial(tp,EFFECT_MUST_BE_XMATERIAL)
	Duel.SetSelectedCard(must)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
	local cancel=Duel.IsSummonCancelable()
	local sg=mg:SelectSubGroup(tp,xyz_goal,cancel,3,99,tp,c)
	if not sg then return false end
	sg:KeepAlive()
	e:SetLabelObject(sg)
	return true
end

function s.xyzop(e,tp,eg,ep,ev,re,r,rp,c,og,min,max)
	local g=e:GetLabelObject() -- selected materials
	-- If any of them had overlays (Xyz), send those to GY by rule first
	local over=Group.CreateGroup()
	for mc in aux.Next(g) do
		local ogp=mc:GetOverlayGroup()
		if #ogp>0 then over:Merge(ogp) end
	end
	if #over>0 then Duel.SendtoGrave(over,REASON_RULE) end
	-- Finish overlay
	c:SetMaterial(g)
	Duel.Overlay(c,g)
	g:DeleteGroup()
end

--========================
-- (Quick) Detach 1 → Negate; also banish if detached was Sanga/Kazejin/Suijin
--========================

-- Cost: select exactly 1 material to detach; store whether it was Sanga/Kazejin/Suijin
function s.ngcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	local og=c:GetOverlayGroup()
	if chk==0 then return #og>0 end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVEXYZ)
	local cg=og:Select(tp,1,1,nil)
	local rc=cg:GetFirst()
	-- Detach by sending to GY as cost (standard for choosing a specific material)
	Duel.SendtoGrave(cg,REASON_COST)
	-- Flag if it was one of the pieces
	if rc and rc:IsCode(CODE_SANGA,CODE_KAZEJIN,CODE_SUIJIN) then
		e:SetLabel(1)
	else
		e:SetLabel(0)
	end
end

function s.ngfilter(c)
	-- Face-up opponent’s card whose effects can be negated
	return c:IsFaceup() and not (c:IsDisabled())
end
function s.ngtg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsOnField() and chkc:IsControler(1-tp) and s.ngfilter(chkc) end
	if chk==0 then return Duel.IsExistingTarget(s.ngfilter,tp,0,LOCATION_ONFIELD,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
	local g=Duel.SelectTarget(tp,s.ngfilter,tp,0,LOCATION_ONFIELD,1,1,nil)
	Duel.SetOperationInfo(0,CATEGORY_DISABLE,g,1,0,0)
	if e:GetLabel()==1 then
		Duel.SetOperationInfo(0,CATEGORY_REMOVE,g,1,0,0)
	end
end
function s.ngop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local tc=Duel.GetFirstTarget()
	if not tc or not tc:IsRelateToEffect(e) or not tc:IsFaceup() then return end
	-- Negate effects until the end of this turn
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_DISABLE)
	e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	tc:RegisterEffect(e1)
	local e2=e1:Clone()
	e2:SetCode(EFFECT_DISABLE_EFFECT)
	tc:RegisterEffect(e2)
	if tc:IsType(TYPE_TRAPMONSTER) then
		local e3=e1:Clone()
		e3:SetCode(EFFECT_DISABLE_TRAPMONSTER)
		tc:RegisterEffect(e3)
	end
	-- If detached one of the pieces, also banish the target
	if e:GetLabel()==1 and tc:IsRelateToEffect(e) and tc:IsAbleToRemove() then
		Duel.Remove(tc,POS_FACEUP,REASON_EFFECT)
	end
end

--========================
-- Float on destruction
--========================
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsPreviousLocation(LOCATION_ONFIELD) and (r&(REASON_BATTLE+REASON_EFFECT))~=0
end
function s.spfilter(c,e,tp)
	-- Level 9 "Gate Guardian" Extra Deck monster (ignore Summon conditions)
	return c:IsLevel(9) and c:IsSetCard(0x52) and c:IsType(TYPE_MONSTER)
		and c:IsCanBeSpecialSummoned(e,0,tp,true,true)
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCountFromEx(tp,tp,nil,e:GetHandler())>0
			and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
end
function s.spop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_EXTRA,0,1,1,nil,e,tp)
	local tc=g:GetFirst()
	if tc then
		Duel.SpecialSummon(tc,0,tp,tp,true,true,POS_FACEUP)
	end
end
